# Imports.
from pydantic import BaseModel


# Define a secret payload model for the API.
class SecretPayload(BaseModel):
    secret: str
