# Imports.
from typing import Dict, List
from datetime import datetime, timezone
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
