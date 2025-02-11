# Imports.
from typing import List
from .interview import Interview
from .participant import Participant
from .prompt import Prompt


# `Condition` class for study conditions.
class Condition:
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
