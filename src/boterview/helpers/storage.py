# Imports.
from typing import List
from datetime import datetime, timezone
from boterview.services.boterview.boterview import Boterview
from boterview.services.boterview.participant import Participant
from boterview.models.database.participant import Participant as ParticipantModel
from boterview.models.database.conversation import Conversation as ConversationModel

# Helpers.
import boterview.helpers.utils as utils


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


# Get the list of conversations for a participant as text.
def get_participant_conversations(participant: ParticipantModel) -> str:
    # Get the list of conversations for the participant.
    conversations: List[ConversationModel] = participant.conversations.order_by(ConversationModel.timestamp) # type: ignore

    # Prepare the output.
    output: str = ""

    # For each conversation.
    for conversation in conversations:
        # Format the conversation.
        output += f"[{conversation.timestamp}] {conversation.message_type.capitalize()}: {conversation.message}" + "\n" # type: ignore

    # Return the conversation text.
    return output


# Parse the `sqlite` database as a `markdown` string.
def parse_database(boterview: Boterview) -> str:
    # Get the current timestamp with timezone information.
    timestamp: str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")

    # Get the study name.
    study_name: str | None = boterview.study.name

    # If the study name is not set, use a default name.
    if not study_name:
        # Set a default study name.
        study_name = "Interview Study"

    # Extract all participants from the database.
    participants: List[ParticipantModel] = ParticipantModel.select()

    # Extract all conversations from the database.
    conversations: List[ConversationModel] = ConversationModel.select()

    # Define commonly used strings.
    new_line: str = "\n"
    empty_line: str = "\n\n"

    # Prepare the markdown content.
    markdown: str = "# Study Output" + empty_line

    markdown += f"This output was generated at {timestamp}." + empty_line

    # Add the study information section.
    markdown += "## Study Information" + empty_line
    markdown += f"- study name: {study_name}" + new_line
    markdown += f"- conditions: {len(boterview.study.conditions)}" + new_line
    markdown += f"- participants: {count_participants(participants)}" + new_line
    markdown += f"- conversations: {count_conversations(conversations)}" + new_line
    markdown += f"- duration: {calculate_duration(participants)} seconds" + empty_line

    # Add the conditions section.
    markdown += "## Conditions" + empty_line

    # For each condition in the study.
    for condition in boterview.study.conditions.values():

        # Add the condition information.
        markdown += f"### {condition.name}" + new_line
        markdown += f"- participants: {count_participants(participants, condition.name)}" + new_line
        markdown += f"- conversations: {count_conversations(conversations, condition.name)}" + new_line
        markdown += f"- duration: {calculate_duration(participants, condition.name)} seconds" + empty_line

        # Add the prompt section.
        markdown += "#### Prompt" + empty_line
        markdown += utils.markdown_code_block(condition.prompt.to_text()) + empty_line

        # Add the interview document section.
        markdown += "#### Interview Document" + empty_line
        markdown += utils.markdown_code_block(condition.interview.to_text().strip()) + empty_line

        # Add the participants section.
        markdown += "#### Participants" + empty_line

        # For each participant in the condition.
        for participant in participants:

            # If the participant is in the condition.
            if participant.condition == condition.name:

                # Add the participant heading.
                markdown += f"##### Participant - {participant.code}" + empty_line

                # Add the participant information.
                markdown += "###### Information" + empty_line
                markdown += f"- id: {participant.id}" + new_line # type: ignore
                markdown += f"- code: {participant.code}" + new_line
                markdown += f"- consent: {participant.consent}" + new_line
                markdown += f"- start time: {participant.start_time}" + new_line
                markdown += f"- end time: {participant.end_time}" + new_line
                markdown += f"- duration: {calculate_participant_duration(participant)} seconds" + empty_line

                # Add the conversation section.
                markdown += "###### Conversation" + empty_line
                markdown += utils.markdown_code_block(get_participant_conversations(participant)) + empty_line

    # Add the participants without consent (i.e., unassigned participants).
    markdown += "## Unassigned Participants" + empty_line

    # Extract the unassigned participants.
    participants_unassigned: List[ParticipantModel] = [participant for participant in participants if not participant.consent]

    # Add the number of unassigned participants.
    markdown += f"- participants: {len(participants_unassigned)}" + empty_line

    # For each participant in the database.
    for participant in participants_unassigned:

        # Add the participant heading.
        markdown += f"### Participant - {participant.code}" + empty_line

        # Add the participant information.
        markdown += "#### Information" + empty_line
        markdown += f"- id: {participant.id}" + new_line # type: ignore
        markdown += f"- code: {participant.code}" + new_line
        markdown += f"- consent: {participant.consent}" + new_line
        markdown += f"- start time: {participant.start_time}" + new_line
        markdown += f"- end time: {participant.end_time}" + new_line
        markdown += f"- duration: {calculate_participant_duration(participant)} seconds" + empty_line

    # Return the markdown.
    return markdown
