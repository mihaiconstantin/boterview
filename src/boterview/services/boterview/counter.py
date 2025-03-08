# Imports.
from typing import List

# Helpers.
import boterview.helpers.utils as utils


# `Counter` class for counting occurrences of conditions and participants.
class Counter:
    # Counter type.
    _counter_type: List[str] = ["conditions", "participants"]

    # Count of conditions.
    conditions: int = 0

    # Count of participants.
    participants: int = 0

    # Increment the count of conditions.
    def increment(self: "Counter", what: str) -> None:
        # If the `what` is for conditions.
        if what == "conditions":
            # Increment the count of conditions.
            self.conditions += 1

        # If the `what` is for participants.
        elif what == "participants":
            # Increment the count of participants.
            self.participants += 1

        # Otherwise.
        else:
            # Raise an error.
            raise ValueError(f"Invalid counter type: \"{what}\". Must be one of {utils.list_to_enumeration(self._counter_type, "or")}.")
