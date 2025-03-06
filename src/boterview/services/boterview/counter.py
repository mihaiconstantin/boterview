# `Counter` class for counting occurrences of conditions and participants.
class Counter:
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
            raise ValueError("Invalid value for `what` argument of `Counter` class.")
