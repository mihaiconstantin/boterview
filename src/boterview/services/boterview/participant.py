# Imports.
import re
from datetime import datetime, timezone
from boterview.services.boterview.conversation import Conversation


# `Participant` class for subjects taking part in the study.
class Participant:
    # The ID.
    code: str

    # The participant consent status.
    consent: bool = False

    # Start time.
    start_time: datetime

    # End time.
    end_time: datetime

    # The condition name.
    condition_name: str

    # The conversation.
    conversation: Conversation

    # System prompt.
    prompt: str

    # Set the conversation.
    def _set_conversation(self: "Participant") -> None:
        # Set the conversation.
        self.conversation = Conversation()

        # Set the participant ID.
        self.conversation.set_participant_code(self.code)

    # Initialize the participant.
    def __init__(self: "Participant", code: str) -> None:
        # Set the ID.
        self.code = code

        # Initialize the start time.
        self.start_time = datetime.now(timezone.utc)

        # Initialize the conversation.
        self._set_conversation()

    # Set the condition name.
    def set_condition_name(self: "Participant", condition_name: str) -> None:
        # Set the name.
        self.condition_name = condition_name

    # Set the system prompt used.
    def set_prompt(self: "Participant", prompt: str) -> None:
        # Compile the `regex` pattern.
        pattern: re.Pattern = re.compile(r"\{\{\s*termination\s*\}\}")

        # Replace the termination pattern and set the prompt.
        self.prompt = pattern.sub("stop " + self.code, prompt)
