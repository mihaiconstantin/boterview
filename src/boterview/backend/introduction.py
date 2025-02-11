# Imports.
from .printable import Printable
from .helpers import read_contents


# `Introduction` class for interview introduction.
class Introduction(Printable):
    # The interview introduction text.
    text: str = ""

    # Initialize the introduction.
    def __init__(self: "Introduction", file: str):
        # Read and set the text from the file.
        self.text = read_contents(file)

    # Prepare text.
    def to_text(self: "Introduction") -> str:
        # Prepare the output text.
        output: str = "## Interview Introduction\n\n"

        # Add the text.
        output += self.text

        # Return the string.
        return output
