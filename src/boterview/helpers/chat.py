# Imports.
from typing import Callable, Dict, List
from datetime import datetime, timezone
import openai
import chainlit
from boterview.services.configuration.configuration import Configuration

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
