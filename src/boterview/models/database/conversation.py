# Imports.
from datetime import datetime, timezone
from peewee import CharField, ForeignKeyField, TextField, Check

# Import models.
from boterview.models.database.base import BaseModel, UTCDateTimeField
from boterview.models.database.participant import Participant


# Define the `Conversation` model.
class Conversation(BaseModel):
    """Conversation model for the database."""

    # The participant.
    participant = ForeignKeyField(
        Participant,
        backref = 'conversations',
        on_delete = 'CASCADE'
    )

    # The message type.
    message_type = CharField(
        max_length = 20,
        column_name = "type",
        constraints = [
            Check("type IN ('bot', 'participant')")
        ]
    )

    # The message content.
    message = TextField()

    # The timestamp.
    timestamp = UTCDateTimeField(default = lambda: datetime.now(timezone.utc))
