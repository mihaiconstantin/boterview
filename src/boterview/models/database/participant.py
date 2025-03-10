# Imports.
from datetime import datetime, timezone
from peewee import BooleanField, CharField, TextField

# Import the base model.
from boterview.models.database.base import BaseModel, UTCDateTimeField


# Define the `Participant` model.
class Participant(BaseModel):
    """Participant model for the database."""

    # The participant code.
    code = CharField(max_length = 100, unique = True)

    # The consent status.
    consent = BooleanField(default = False)

    # The participant condition.
    condition = CharField(null = True, max_length = 100)

    # The participant interview prompt.
    prompt = TextField(null = True)

    # The start time.
    start_time = UTCDateTimeField(default = lambda: datetime.now(timezone.utc))

    # The end time of the chat.
    end_time = UTCDateTimeField(null = True)
