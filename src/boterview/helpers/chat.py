# Imports.
from typing import Dict
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
