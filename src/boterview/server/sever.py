# Imports.
from fastapi import FastAPI

# Database models.
from boterview.models.database.conversation import Conversation
from boterview.models.database.participant import Participant

# Import the context.
import boterview.context.persistence as persistence


# Define a lifespan function factory.
def create_lifespan(database: str):
    # Local imports.
    from contextlib import asynccontextmanager

    # Define the lifespan event handler.
    @asynccontextmanager
    async def lifespan(server: FastAPI):
        # Startup.

        # Initialize the database connection.
        persistence.initialize_database(database)

        # Create the tables.
        persistence.database.create_tables([Participant, Conversation])

        # Yield control to the server.
        yield

        # Shutdown.

        # Close the database connection.
        persistence.database.close()

    # Return the lifespan event handler.
    return lifespan
