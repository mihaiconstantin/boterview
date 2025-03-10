# Imports.
from boterview.models.database.participant import Participant as ParticipantModel


# Get the participant from the database by code.
def get_participant(code: str) -> ParticipantModel:
    # Get the participant from the database by code.
    participant: ParticipantModel = ParticipantModel.get(ParticipantModel.code == code)

    # Return the participant.
    return participant
