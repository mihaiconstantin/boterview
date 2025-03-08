# Imports.
from boterview.services.boterview.printable import Printable

# Helpers.
import boterview.helpers.utils as utils


# `Prompt` class for model.
class Prompt(Printable):
    # The model system prompt text.
    text: str = ""

    # Initialize the prompt.
    def __init__(self: "Prompt", file: str):
        # Read and set the text from the file.
        self.text = utils.read_contents(file)

    # Prepare text.
    def to_text(self: "Prompt") -> str:
        # Return the string.
        return self.text
