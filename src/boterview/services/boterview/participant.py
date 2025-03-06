# Imports.
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

    # Initialize the participant.
    def __init__(self: "Participant", code: str) -> None:
        # Set the ID.
        self.code = code

        # Initialize the condition name.
        self.condition = None

    # Set the condition name.
    def set_condition_name(self: "Participant", condition_name: str) -> None:
        # Set the name.
        self.condition_name = condition_name

    # Set the conversation.
    def _set_conversation(self: "Participant") -> None:
        # Set the conversation.
        self.conversation = Conversation()

        # Set the participant ID.
        self.conversation.set_participant_code(self.code)
