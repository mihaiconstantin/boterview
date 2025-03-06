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
        self.text = text
        self.note = note

    # Prepare text version of the question.
    def to_text(self: "Question") -> str:
        # Prepare the string.
        output: str = f"Question. { self.text }"

        # If there is a note.
        if self.note:
            # Add a new line.
            output += "\n"

            # Add the note to the string.
            output += f"Note. { self.note }"

        # Return the string.
        return output
