# Imports.
from typing import List
from boterview.services.boterview.printable import Printable
from boterview.services.boterview.interview import Interview
from boterview.services.boterview.participant import Participant
from boterview.services.boterview.prompt import Prompt


# `Condition` class for study conditions.
class Condition(Printable):
    # Condition name.
    name: str

    # Prompt object.
    prompt: Prompt

    # Interview object.
    interview: Interview

    # Assigned participants.
    participants: List[Participant]

    # Initialize the condition.
    def __init__(self: "Condition", name: str, prompt: Prompt, interview: Interview) -> None:
        # Set the condition name.
        self.name = name

        # Set the prompt object.
        self.prompt = prompt

        # Set the interview object.
        self.interview = interview

        # Initialize an empty list of participants.
        self.participants = []

    # Append a participant.
    def append_participant(self: "Condition", participant: Participant) -> None:
        # Append the participant.
        self.participants.append(participant)

        # Also set the condition name on the participant.
        participant.set_condition_name(self.name)

        # As well as the system prompt.
        participant.set_prompt(self.to_text())

    # Render the condition as text.
    def to_text(self: "Condition") -> str:
        # Add the prompt.
        text: str = self.prompt.to_text()

        # Add an empty line.
        text += "\n\n"

        # Add the interview.
        text += self.interview.to_text()

        # Return the string.
        return text
