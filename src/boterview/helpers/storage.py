# Imports.
from typing import List
from boterview.services.boterview.participant import Participant
from boterview.models.database.participant import Participant as ParticipantModel
from boterview.models.database.conversation import Conversation as ConversationModel


# Get the participant from the database by code.
def get_participant(code: str) -> ParticipantModel:
    # Get the participant from the database by code.
    participant: ParticipantModel = ParticipantModel.get(ParticipantModel.code == code)

    # Return the participant.
    return participant


# Save participant to the sqlite database.
def save_participant(participant: Participant) -> ParticipantModel:
    # Create a participant model and insert the record into the database.
    participant_model: ParticipantModel = ParticipantModel.create(
        code = participant.code,
        consent = participant.consent,
        start_time = participant.start_time,
        condition = participant.condition_name,
        prompt = participant.prompt
    )

    # Return the created participant record.
    return participant_model


# Save conversation to the sqlite database.
def save_conversation(participant_model: ParticipantModel, message_type: str, message: str) -> ConversationModel:
    # Create a conversation model and insert the record into the database.
    conversation_model: ConversationModel = ConversationModel.create(
        participant = participant_model,
        message_type = message_type,
        message = message
    )

    # Return the created conversation record.
    return conversation_model


# Count how many participants the study had.
def count_participants(participants: List[ParticipantModel], condition_name: str | None = None) -> int:
    # Define the count.
    count: int

    # If the condition is not provided, get the total count.
    if not condition_name:
        # Count.
        count = len(participants)

    # Otherwise, count the participants based on the condition.
    else:
        # Count
        count = len([
            participant for
            participant in participants if
            participant.condition == condition_name
        ])

    # Return the count.
    return count


# Count how many conversations the study had.
def count_conversations(conversations: List[ConversationModel], condition_name: str | None = None) -> int:
    # Define the count.
    count: int

    # If the condition is not provided, get the total count.
    if not condition_name:
        # Count.
        count = len(conversations)

    # Otherwise, count the conversations based on the condition.
    else:
        # Count.
        count = len([
            conversation for
            conversation in conversations if
            conversation.participant.condition == condition_name
        ])

    # Return the count.
    return count


# Calculate the total duration of the study.
def calculate_duration(participants: List[ParticipantModel], condition_name: str | None = None) -> int:
    # Define the total duration.
    total_duration: int = 0

    # If the condition is not provided, calculate the total duration.
    if not condition_name:
        # Calculate the total duration.
        for participant in participants:
            # If both the start and the end times are set.
            if participant.start_time and participant.end_time:
                # Calculate the duration.
                total_duration += (participant.end_time - participant.start_time).seconds

    # Otherwise, calculate the duration for the given condition.
    else:
        # Calculate the total duration for the condition.
        for participant in participants:
            # If the condition matches.
            if participant.condition == condition_name:
                # If both the start and the end times are set.
                if participant.start_time and participant.end_time:
                    # Calculate the duration.
                    total_duration += (participant.end_time - participant.start_time).seconds

    # Return.
    return total_duration


# Calculate the duration for a single participant.
def calculate_participant_duration(participant: ParticipantModel) -> int:
    # Default duration.
    duration: int = 0

    # If both the start and the end times are set.
    if participant.start_time and participant.end_time:
        # Calculate the duration.
        duration = (participant.end_time - participant.start_time).seconds

        # Return the duration.
        return duration

    # Return the default duration.
    return duration
