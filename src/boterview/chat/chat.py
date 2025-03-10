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

    # Get the message history.
    message_history: List[Dict[str, str]] = chat.get_message_history()

    # Set the system prompt in the session.
    message_history.append({"role": "system", "content": participant.prompt})

    # Send an initial message.
    await chainlit.Message(content = configuration.data["chat"]["initial_message"]).send()

    # Get the bot response.
    response = await get_bot_response(message_history)

    # Append the bot's response to the history.
    message_history.append({"role": "assistant", "content": response.content})

    # Save the conversation to the database.
    storage.save_conversation(participant_model, "bot", response.content)

    # Send the message.
    await response.update()
