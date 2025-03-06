# Imports.
from boterview.backend.printable import Printable
from boterview.backend.helpers import read_contents


# `Closing` class for interview closing.
class Closing(Printable):
    # The interview closing text.
    text: str = ""

    # Initialize the closing.
    def __init__(self: "Closing", file: str):
        # Read and set the text from the file.
        self.text = read_contents(file)

    # Prepare text.
    def to_text(self: "Closing") -> str:
        # Prepare the output text.
        output: str = "## Interview Closing\n\n"

        # Add the text.
        output += self.text

        # Return the string.
        return output
