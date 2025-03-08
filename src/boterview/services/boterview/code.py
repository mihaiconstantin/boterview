# `Code` class for representing a participation code.
class Code:
    # Code value.
    value: str

    # The used status of the code.
    used: bool

    # Initialize the code.
    def __init__(self: "Code", value: str) -> None:
        # Set the code value.
        self.value = value

        # Set the used status of the code.
        self.used = False
