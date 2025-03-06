# Imports.
from typing import List
import re
from boterview.services.configuration.configuration import Configuration
from boterview.services.boterview.printable import Printable
from boterview.services.boterview.question import Question

# Helpers.
import boterview.helpers.utils as utils


# `Protocol` class.
class Protocol(Printable):
    # The questions array.
    questions: List[Question] = []

    # Get the question identifier.
    def _get_question_identifier(self: "Protocol", question_text: str) -> str:
        # Define the question annotation pattern.
        pattern: re.Pattern = re.compile(r"^(?P<annotation>Question)\s?(?P<identifier>[a-zA-Z]|[0-9]+[a-zA-Z]?)*(?P<period>\.)")

        # Extract the match.
        match: re.Match[str] | None = pattern.match(question_text)

        # If there is a match.
        if match:
            # Extract the identifier.
            identifier = match.group("identifier")

            # Return the identifier.
            return identifier

        # Otherwise, return an empty string.
        return ""

    # Remove the question annotation.
    def _remove_question_annotation(self: "Protocol", question_text: str) -> str:
        # Define the question annotation pattern.
        pattern: re.Pattern = re.compile(r"^Question\s?([a-zA-Z]|[0-9]+[a-zA-Z]?)*\.")

        # Remove the question annotation.
        result: str = pattern.sub("", question_text).strip()

        # Return the note.
        return result

    # Remove the note identifier.
    def _remove_note_annotation(self: "Protocol", question_note: str) -> str:
        # Define the note annotation pattern.
        pattern: re.Pattern = re.compile(r"^Note\.")

        # Remove the note annotation.
        result: str = pattern.sub("", question_note).strip()

        # Return the note.
        return result

    # Parse the questions.
    def _parse_questions(self: "Protocol", file: str, question_separator: str) -> List[Question]:
        # Initialize the list of questions.
        questions: List[Question] = []

        # Split contents by empty lines.
        blocks: List[str] = self.raw.split(question_separator)

        # For each block containing the question and the note.
        for index, block in enumerate(blocks):
            # Remove leading and trailing whitespace.
            block = block.strip()

            # If the block is empty.
            if not block:
                # Skip it.
                continue

            # Split the block by empty line and extract the split as the question.
            lines: List[str] = block.split("\n\n")

            # Extract the question text.
            question_text: str = " ".join(lines[0].strip().split("\n"))

            # Extract the question note.
            question_note: str = "\n\n".join(lines[1:]).strip()

            # Remove the question annotation.
            question_text = self._remove_question_annotation(question_text)

            # Remove the note annotation.
            question_note = self._remove_note_annotation(question_note)

            # Initialize the question.
            question: Question = Question(text = question_text, note = question_note)

            # Append the question to the list.
            questions.append(question)

        # Return the list of questions.
        return questions

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
