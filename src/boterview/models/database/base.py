# Imports.
from datetime import datetime
from peewee import Model, DateTimeField

# Import the context.
import boterview.context.persistence as persistence


# Define the base model for the database.
class BaseModel(Model):
    """Base model for the database."""
    class Meta:
        database = persistence.database


# Define a custom `DateTimeField` for UTC timestamps (i.e., ISO 8601 compliant).
class UTCDateTimeField(DateTimeField):
    # Convert the `Python` value to the database value.
    def python_value(self, value):

        # Use the default implementation.
        value = super().python_value(value)

        # If it is a string.
        if isinstance(value, str):
            # Convert it to a `datetime` object.
            date: datetime = datetime.fromisoformat(value)

            # Return the converted string.
            return date

        # Otherwise, return the value.
        return value
