# Imports.
from typing import Callable, Dict, List
import chainlit
import openai
from boterview.services.boterview.participant import Participant
from boterview.services.configuration.configuration import Configuration
from boterview.services.boterview.boterview import Boterview

# Import helpers.
import boterview.helpers.authentication as authentication
import boterview.helpers.chat as chat
import boterview.helpers.storage as storage

# Import the database models.
from boterview.models.database.participant import Participant as ParticipantModel

# Import the context.
import boterview.context.app as app
import boterview.context.bot as bot


# Get the configuration.
configuration: Configuration = app.get_configuration()

# Get the `boterview` object.
boterview: Boterview = app.get_boterview()

# Create a chat client.
client: openai.AsyncClient = bot.get_openai_client(configuration)

# Extract the model settings from the configuration.
client_settings = configuration.data["bot"]["settings"]

# Prepare the client callable.
get_bot_response: Callable = chat.get_bot_response_setup(client, client_settings)


# On user authentication.
@chainlit.header_auth_callback # type: ignore
def header_auth_callback(headers: Dict) -> chainlit.User | None:
    # If the cookie header is not present.
    if not (cookie := headers.get("cookie")):
        # Signal unauthenticated.
        return None

    # Parse the cookie header.
    cookies: Dict[str, str] = authentication.parse_cookie(cookie)

    # Attempt to decode the JWT.
    try:
        # Decode the JWT.
        code: str = authentication.decode_jwt(cookies["code"])

    # Catch any exceptions.
    except Exception:
        # Signal unauthenticated.
        return None

    # Return the user to signal authentication.
    return chainlit.User(identifier = code)


# On chat start.
@chainlit.on_chat_start
async def on_start():
    # Get the user from the session.
    user: chainlit.User | None = chainlit.user_session.get("user")

    # # If the user is not present, return.
    if not user:
        return

    # Randomly assign a new participant to one of the study conditions.
    boterview.assign_participant(user.identifier)

    # Get the assigned participant object.
    participant: Participant = boterview.retrieve_participant(user.identifier)

    # Get the participant model from the database by the code.
    participant_model: ParticipantModel = storage.get_participant(participant.code)

    # Update the participant condition.
    participant_model.condition = participant.condition_name # type: ignore

    # Update the participant prompt.
    participant_model.prompt = participant.prompt # type: ignore

    # Save the participant record.
    participant_model.save()

    # Get the stored message history from the database with the system prompt.
    chat.initialize_message_history(participant_model)

    # Populate the chat interface with any previous messages.
    await chat.populate_chat_interface(participant_model)

    # Get the possibly restored session message history.
    message_history: List[Dict[str, str]] = chat.get_message_history()

    # Get the last message role.
    last_message: Dict[str, str] = message_history[-1]

    # Get the last role from the last message.
    last_role: str = last_message["role"]

    # If the last message was from the bot (i.e., assistant).
    if last_role == "assistant":
        # The wait for the user's response.
        return

    # If the last message was not the system prompt.
    if last_role != "system":
        # If the last message contained the stop command.
        if chat.should_stop_chatting(last_message["content"], participant.code):
            # The wait for the user's reaction before anything else.
            return

    # Otherwise, if the last message is the system prompt.
    if last_role == "system":
        # Send an initial message.
        await chainlit.Message(content = configuration.data["chat"]["initial_message"]).send()

    # Otherwise, if the last message was from the user.
    elif last_role == "user":
        # Send a resume message.
        await chainlit.Message(content = configuration.data["chat"]["resume_message"]).send()

    # Get the bot response.
    response = await get_bot_response(message_history)

    # Append the bot's response to the history.
    message_history.append({"role": "assistant", "content": response.content})

    # Save the conversation to the database.
    storage.save_conversation(participant_model, "bot", response.content)

    # Send the message.
    await response.update()


# On chat message.
@chainlit.on_message
async def on_message(message: chainlit.Message):
    # Get the user from the session.
    user: chainlit.User | None = chainlit.user_session.get("user")

    # If the user is not present, return.
    if not user:
        return

    # Get the participant object.
    participant: Participant | None = boterview.study.get_participant(user.identifier)

    # If the participant is not found, return.
    if not participant:
        return

    # Get the participant model.
    participant_model: ParticipantModel = storage.get_participant(participant.code)

    # Get the message history.
    message_history: List[Dict[str, str]] = chat.get_message_history()

    # Append the user's message to the history.
    message_history.append({"role": "user", "content": message.content})

    # Save the conversation to the database.
    storage.save_conversation(participant_model, "participant", message.content)

    # If the user's message contains the stop command.
    if chat.should_stop_chatting(message.content, participant.code):
        # Send a stop message.
        return await chat.send_stop_message(
            content = configuration.data["chat"]["stop_response_user_triggered"],
            payload = chat.stop_payload(participant.code, message.content)
        )

    # Get the bot response.
    response = await get_bot_response(message_history)

    # Append the bot's response to the history.
    message_history.append({"role": "assistant", "content": response.content})

    # Save the conversation to the database.
    storage.save_conversation(participant_model, "bot", response.content)

    # If the bot's message contains the stop command.
    if chat.should_stop_chatting(response.content, participant.code):
        # Remove the last response from the UI.
        await response.remove()

        # Send a stop message.
        return await chat.send_stop_message(
            content = configuration.data["chat"]["stop_response_bot_triggered"],
            payload = chat.stop_payload(participant.code, message.content)
        )

    # Send the message.
    await response.update()


# On interview termination notice (i.e., either user or bot triggered).
@chainlit.action_callback("on_stop")
def on_stop(action: chainlit.Action):
    # Return.
    return "stop"


# On chat end (i.e., when the user leaves the `/chat/` endpoint).
@chainlit.on_chat_end
def on_end():
    ...
