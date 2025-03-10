# Imports.
import openai
from boterview.services.configuration.configuration import Configuration


# Create an `OpenAI` client.
_client: openai.AsyncOpenAI | None = None


# Get the `OpenAI` client.
def get_openai_client(configuration: Configuration) -> openai.AsyncOpenAI:
    # Access the global variables.
    global _client

    # If the client is not yet initialized.
    if _client is None:
        # Create a new `OpenAI` client.
        _client = openai.AsyncOpenAI(
            # Set the API key.
            api_key = configuration.data["bot"]["api_key"]
        )

    # Assert the client is not `None`.
    assert _client is not None, "`OpenAI` client not initialized."

    # Return the client.
    return _client
