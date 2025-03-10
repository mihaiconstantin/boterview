# Imports.
from boterview.services.boterview.participant import Participant
from boterview.models.database.participant import Participant as ParticipantModel


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
