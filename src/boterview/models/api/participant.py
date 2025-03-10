# Imports.
from pydantic import BaseModel


# Define a participant payload model for the API.
class ParticipantPayload(BaseModel):
    code: str
    verified: bool
    consented: bool
