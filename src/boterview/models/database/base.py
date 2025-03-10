# Imports.
from peewee import Model

# Import the context.
import boterview.context.persistence as persistence


# Define the base model for the database.
class BaseModel(Model):
    """Base model for the database."""
    class Meta:
        database = persistence.database
