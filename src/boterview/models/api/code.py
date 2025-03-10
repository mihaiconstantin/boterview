# Imports.
from pydantic import BaseModel


# Define a code payload model for the API.
class CodePayload(BaseModel):
    code: str
