# Imports.
from boterview.services.boterview.printable import Printable
import boterview.helpers.utils as utils


# `Guide` class for interview background information.
class Guide(Printable):
    # The interview guide text.
    text: str = ""

    # Parse the guide text.
    def _parse_file(self: "Guide", file: str | None) -> None:
        # If the file is not set.
        if not file:
            # Return
            return

        # Otherwise, read and set the text from the file.
        self.text = utils.read_contents(file)

    # Initialize the guide.
    def __init__(self: "Guide", file: str | None):
        # Parse the text.
        self._parse_file(file)

    # Prepare text.
    def to_text(self: "Guide") -> str:
        # If the text is empty, return an empty string.
        if not self.text:
            # Return
            return ""

        # Otherwise, prepare the output text.
        output: str = "## Interview Guide\n\n"

        # Add the text.
        output += self.text

        # Return the string.
        return output
