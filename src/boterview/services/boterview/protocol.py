# Imports.
from typing import List
from boterview.services.configuration.configuration import Configuration
from boterview.services.boterview.printable import Printable
from boterview.services.boterview.question import Question

# Helpers.
import boterview.helpers.utils as utils


# `Protocol` class.
class Protocol(Printable):
    # The questions array.
    questions: List[Question] = []

    # Initialize the protocol.
    def __init__(self: "Protocol", file: str):
        # Parse the questions.
        self.questions = parse_questions(file)

    # Prepare text version of the protocol.
    def to_text(self: "Protocol") -> str:
        # Initialize the text.
        text: str = "## Interview Questions\n\n"

        # For each question.
        for index, question in enumerate(self.questions):
            # Add the question to the text.
            text += question.to_text()

            # If it's not the last question.
            if index < len(self.questions) - 1:
                # Add a new line.
                text += "\n\n"

        # Return the text.
        return text
