# Imports.
from typing import List, Dict
from datetime import datetime, timezone
from boterview.services.boterview.printable import Printable

# Helpers.
import boterview.helpers.utils as utils


# `Conversation` class for the chat between the bot and the participant.
class Conversation(Printable):
    # Allowed message types.
    _message_type: List[str] = ["bot", "participant"]

    # Participant code (i.e., aka ID).
    participant_code: str

    # History.
    history: List[Dict[str, str]]

    # Initialize the conversation.
    def __init__(self: "Conversation") -> None:
        # Initialize an empty history.
        self.history = []

    # Set the participant code.
    def set_participant_code(self: "Conversation", participant_code: str) -> None:
        # Set the participant code.
        self.participant_code = participant_code

    # Append a message to the history.
    def append_message(self: "Conversation", type: str, message: str) -> None:
        # Validate the message type.
        if type not in self._message_type:
            # Throw.
            raise ValueError(f"Invalid conversation message type: \"{type}\". Must be one of {utils.list_to_enumeration(self._message_type, "or")}.")

        # Append the message to the history.
        self.history.append({
            "type": type,
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
            "message": message
        })

    # Convert the conversation to text.
    def to_text(self: "Conversation") -> str:
        # Initialize the text.
        text: str = ""

        # For each message in the history.
        for message in self.history:
            # Add the message to the text.
            text += f"{message["timestamp"]} - {message["type"].capitalize()}: {message["message"]}\n"

        # Return the text.
        return text
