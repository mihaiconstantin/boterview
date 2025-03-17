# Imports.
from typing import Callable, Dict, List, Literal
from datetime import datetime, timezone
import openai
import chainlit
from boterview.services.configuration.configuration import Configuration

# Import the database models.
from boterview.models.database.participant import Participant as ParticipantModel
from boterview.models.database.conversation import Conversation as ConversationModel

# Import the application context.
import boterview.context.app as app


# Define function to check if the chat should be stopped.
def should_stop_chatting(message: str, user_code: str) -> bool:
    # Check if the message contains the stop command.
    stop: bool = "stop" in message.lower() and user_code.lower() in message.lower()

    # Return.
    return stop


# Define a function to send a stop message.
async def send_stop_message(content: str,  callback: str = "on_stop", payload: Dict = {}) -> None:
    # Get the configuration.
    configuration: Configuration = app.get_configuration()

    # Send the message.
    await chainlit.Message(
        content = content,
        actions = [
            chainlit.Action(
                name = callback,
                payload = payload,
                icon = "power",
                label = configuration.data["chat"]["stop_button_label"]
            )
        ]
    ).send()


# Define the termination payload.
def stop_payload(user_code: str, message: str) -> Dict:
    return {
        "user": user_code,
        "stopped_at": datetime.now(timezone.utc).isoformat(),
        "message": message
    }


# Get the message history in the `chainlit` session.
def get_message_history() -> List[Dict[str, str]]:
    # Attempt to get the `chainlit` message history.
    message_history: List[Dict[str, str]] | None = chainlit.user_session.get("message_history")

    # If the message history is not present.
    if message_history is None:
        # Set the message history to an empty list.
        message_history = []

        # Initialize the session message history to an empty list.
        chainlit.user_session.set("message_history", message_history)

    # Return the message history.
    return message_history


# Initialize the message history in the `chainlit` session.
def initialize_message_history(participant: ParticipantModel) -> None:
    # Get the message history.
    message_history: List[Dict[str, str]] = get_message_history()

    # If there exists a message history.
    if message_history:
        # Return.
        return

    # Otherwise, set the system prompt in the session.
    message_history.append({
        "role": "system",
        "content": participant.prompt # type: ignore
    })

    # If the participant has conversations stored.
    if participant.conversations.exists(): # type: ignore
        # Get previously stored conversations.
        conversations: List[ConversationModel] =  participant.conversations.order_by(ConversationModel.timestamp) # type: ignore

        # For each conversation.
        for conversation in conversations:
            # Determine the role from the message type.
            role = "assistant" if conversation.message_type == "bot" else "user"

            # Update the session message history to include the conversation.
            message_history.append({
                "role": role,
                "content": str(conversation.message)
            })

    # Return (i.e., no need to set to session since dealing with a reference).
    return


# Populate the chat interface from the message history.
async def populate_chat_interface(participant: ParticipantModel) -> None:
    # Get the message history.
    message_history: List[Dict[str, str]] = get_message_history()

    # If the history is empty.
    if not message_history:
        # Return.
        return None

    # Define the message types that conform the the `literalai` `MessageStepType` type.
    types: Dict[str, Literal["assistant_message", "user_message", "system_message"]] = {
        "assistant": "assistant_message",
        "user": "user_message",
        "system": "system_message"
    }

    # Get the application configuration.
    configuration: Configuration = app.get_configuration()

    # Otherwise, for each message in the history.
    for message in message_history:
        # If the message is a system message.
        if message["role"] == "system":
            # Skip.
            continue

        # Check if the message triggers a stop.
        stop_triggered = should_stop_chatting(message["content"], participant.code) # type: ignore

        # Always display the user message or any other message not triggering a stop.
        if message["role"] == "user" or not stop_triggered:
            # Display the message.
            await chainlit.Message(
                content = message["content"],
                type = types[message["role"]]
            ).send()

        # However, if the message triggered a stop.
        if stop_triggered:
            # And if the assistant is the culprit.
            if message["role"] == "assistant":
                # Replace the assistant message with a stop message.
                await send_stop_message(
                    content = configuration.data["chat"]["stop_response_bot_triggered"],
                    payload = stop_payload(participant.code, message["content"]) # type: ignore
                )

            # Otherwise, respond on behalf oath assistant with a stop message.
            else:
                # Send a stop message as a response.
                await send_stop_message(
                    content = configuration.data["chat"]["stop_response_user_triggered"],
                    payload = stop_payload(participant.code, message["content"]) # type: ignore
                )


# Get a message from the LLM.
def get_bot_response_setup(client: openai.AsyncOpenAI, client_settings: Dict[str, str]) -> Callable:
    # Define the get bot response function.
    async def get_bot_response(message_history: List[Dict[str, str]], author: str = "Interviewer") -> chainlit.Message:
        # Create a message object for the bot response.
        response: chainlit.Message = chainlit.Message(content = "", author = author)

        # Get the stream.
        stream = await client.chat.completions.create(messages = message_history, stream = True, **client_settings) # type: ignore

        # For each part in the stream.
        async for part in stream:
            # If the part has a message.
            if token := part.choices[0].delta.content or "":
                # Wait for the response.
                await response.stream_token(token)

        # Return the response.
        return response

    # Return the function.
    return get_bot_response
