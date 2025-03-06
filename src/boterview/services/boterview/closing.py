# Imports.
from boterview.services.boterview.printable import Printable

# Helpers.
import boterview.helpers.utils as utils


# `Closing` class for interview closing.
class Closing(Printable):
    # The interview closing text.
    text: str = ""

    # Parse the guide text.
    def _parse_file(self: "Closing", file: str | None) -> None:
        # If the file is not set.
        if not file:
            # Return
            return

        # Otherwise, read and set the text from the file.
        self.text = utils.read_contents(file)

    # Initialize the closing.
    def __init__(self: "Closing", file: str | None):
        # Parse the text.
        self._parse_file(file)

    # Prepare text.
    def to_text(self: "Closing") -> str:
        # If the text is empty, return an empty string.
        if not self.text:
            # Return
            return ""

        # Otherwise, prepare the output text.
        output: str = "## Interview Closing\n\n"

        # Add the text.
        output += self.text

        # Return the string.
        return output
