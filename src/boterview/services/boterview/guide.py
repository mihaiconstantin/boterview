# Imports.
from boterview.services.boterview.printable import Printable
import boterview.helpers.utils as utils


# `Guide` class for interview background information.
class Guide(Printable):
    # The interview guide text.
    text: str = ""

    # Initialize the guide.
    def __init__(self: "Guide", file: str):
        # Read and set the text from the file.
        self.text = read_contents(file)

    # Prepare text.
    def to_text(self: "Guide") -> str:
        # Prepare the output text.
        output: str = "## Interview Guide\n\n"

        # Add the text.
        output += self.text

        # Return the string.
        return output
