# Imports.
from typing import Dict, List
import random
from boterview.services.boterview.code import Code
from boterview.services.boterview.condition import Condition
from boterview.services.boterview.participant import Participant
from boterview.services.boterview.counter import Counter


# `Study` class for conducting interviews.
class Study:
    # Study name.
    name: str | None

    # Generic counter.
    counter: Counter

    # Participation codes.
    codes: List[Code]

    # Dictionary of conditions.
    conditions: Dict[str, Condition]

    # Initialize the study.
    def __init__(self: "Study") -> None:
        # Initialize the counter.
        self.counter = Counter()

        # Initialize an empty list of conditions.
        self.conditions = {}

    # Set the study name.
    def set_name(self: "Study", name: str) -> None:
        # Set the study name.
        self.name = name

    # Set the participation codes.
    def set_codes(self: "Study", codes: List[Code]) -> None:
        # Set the participation codes.
        self.codes = codes

    # Append a condition.
    def append_condition(self: "Study", condition: Condition) -> None:
        # Append the condition to the dictionary.
        self.conditions.update({ condition.name: condition })

        # Increment the conditions counter.
        self.counter.increment(what = "conditions")

    # Randomly assign a participant to a condition, but keep the number of participants in each condition balanced.
    def assign_participant(self: "Study", participant: Participant) -> None:
        # Find the minimum number of participants assigned to a condition.
        smallest_allocation: int = min(
            len(c.participants) for c in self.conditions.values()
        )

        # Get all conditions with that are subject to the smallest allocation.
        eligible_conditions: List[Condition] = [
            c for c in self.conditions.values() if len(c.participants) == smallest_allocation
        ]

        # Get a condition among those with the smallest allocation.
        condition: Condition = random.choice(eligible_conditions)

        # Assign the participant to the condition.
        condition.append_participant(participant)

        # Increment the participants counter.
        self.counter.increment(what = "participants")

    # Get a participation object by code.
    def get_participant(self: "Study", code: str) -> Participant | None:
        # Find the participant in the conditions.
        participant: Participant | None = next(
            (p for c in self.conditions.values() for p in c.participants if p.code == code), None
        )

        # Return the participant.
        return participant
