# Imports.
from datetime import datetime
from typing import List, Dict
from boterview.backend.printable import Printable


# `Conversation` class for the chat between the bot and the participant.
class Conversation(Printable):
    # Participant ID.
    participant_id: str

    # History.
    history: List[Dict[str, str]]

    # Initialize the conversation.
    def __init__(self: "Conversation") -> None:
        # Initialize an empty history.
        self.history = []

    # Set the participant ID.
    def set_participant_id(self: "Conversation", participant_id: str) -> None:
        # Set the participant ID.
        self.participant_id = participant_id

    # Append a message to the history.
    def append_message(self: "Conversation", type: str, message: str) -> None:
        # Validate the message type.
        if type not in ["bot", "participant"]:
            raise ValueError(f"Invalid conversation message type: '{type}'.")

        # Append the message to the history.
        self.history.append({
            "type": type,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "message": message
        })

    # Convert the conversation to text.
    def to_text(self: "Conversation") -> str:
        # Initialize the text.
        text: str = ""

        # For each message in the history.
        for message in self.history:
            # Add the message to the text.
            text += f"{message['timestamp']} - {message['type'].capitalize()}: {message['message']}\n"

        # Return the text.
        return text
