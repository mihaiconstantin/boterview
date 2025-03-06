# Imports.
from boterview.backend.printable import Printable
from boterview.backend.helpers import read_contents


# `Prompt` class for model.
class Prompt(Printable):
    # The model system prompt text.
    text: str = ""

    # Initialize the prompt.
    def __init__(self: "Prompt", file: str):
        # Read and set the text from the file.
        self.text = read_contents(file)

    # Prepare text.
    def to_text(self: "Prompt") -> str:
        # Return the string.
        return self.text
