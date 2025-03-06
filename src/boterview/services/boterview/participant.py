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
    condition_name: str | None

    # The conversation.
    conversation: Conversation

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
    def set_conversation(self: "Participant", conversation: Conversation) -> None:
        # Set the conversation.
        self.conversation = conversation

        # Set the participant ID.
        self.conversation.set_participant_id(self.id)
