# Imports.
from typing import List
from boterview.backend.question import Question


# Helper to read the questions from a file and return them as a list.
def parse_questions(file: str) -> List[Question]:
    """
    Read the questions from a file and return them as a list. Each question
    contains of two elements, the text for the question itself, and a note
    associated with the question. The first line always contains the question,
    and the second line always contains the note. Therefore, a question occupies
    two lines of text. It is possible for a question to not have a note.
    Questions are separated in the file by an empty line. The order of the
    questions in the file reflects their order during the interview. For
    example, the following indicates contains three questions:

        Question. What is the capital of France? Note. This question may be
        skipped for non-European participants.

        Question. What is the meaning of life?

        Question. Why is your opinion about universal basic income? Note. This
        question is not optional.
    """
    # Open the file
    with open(file, "r") as f:
        content = f.read()

    # Initialize the list of questions.
    questions: List[Question] = []

    # Split content by empty lines.
    blocks = content.split("\n\n")

    # For each block containing the question and the note.
    for block in blocks:
        # Remove leading and trailing whitespace.
        block = block.strip()

        # If the block is empty.
        if not block:
            # Skip it.
            continue

        # If the block has a note.
        if "Note." in block:
            # Split the block by the `Note.` string.
            parts = block.split("Note.", 1)

            # Extract the question text part.
            text = parts[0].strip()

            # Extract the note part.
            note = parts[1].strip()
        # Otherwise.
        else:
            # The question text is the entire block.
            text = block.strip()

            # THe note is empty.
            note = None

        # Remove the `Question.` string from the question text.
        text = text.replace("Question.", "").strip()

        # Initialize the question object.
        question: Question = Question(text, note)

        # Append the question to the list of questions.
        questions.append(question)

    # Return the list of questions.
    return questions


# Parse the contents of a file.
def read_contents(file: str) -> str:
    """
    Read the contents of a file and return them as a string.
    """
    # Open the file.
    with open(file, "r") as f:
        # Read the contents.
        content = f.read()

    # Remove leading and trailing whitespace.
    content = content.strip()

    # Return the contents.
    return content
