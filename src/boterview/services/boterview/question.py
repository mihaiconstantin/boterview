# Imports.
from boterview.services.boterview.printable import Printable


# `Question` class.
class Question(Printable):
    # The question text.
    text: str

    # The question note.
    note: str | None

    # Initialize the question.
    def __init__(self: "Question", text: str, note: str | None) -> None:
        # Set the question text.
        self.text = text

        # Set the question note.
        self.note = note

    # Prepare text version of the question.
    def to_text(self: "Question", **kwargs) -> str:
        # Get the question number if any.
        number: str = str(kwargs.get("number", ""))

        # If there is no text for the question.
        if not self.text:
            # Return an empty string.
            return ""

        # Otherwise, prepare the output text.
        output: str = "### Question " + number + "\n\n"

        # Add the question text.
        output += self.text

        # If there is a note.
        if self.note:
            # Add a new line.
            output += "\n\n"

            # Add the note header.
            output += "**Note.**\n\n"

            # Add the note to the string.
            output += self.note

        # Return the string.
        return output
