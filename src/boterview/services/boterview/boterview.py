# Imports.
from typing import List
from boterview.services.boterview.code import Code
from boterview.services.boterview.participant import Participant
from boterview.services.boterview.study import Study
from boterview.services.boterview.protocol import Protocol
from boterview.services.boterview.introduction import Introduction
from boterview.services.boterview.closing import Closing
from boterview.services.boterview.guide import Guide
from boterview.services.boterview.interview import Interview
from boterview.services.boterview.condition import Condition
from boterview.services.boterview.prompt import Prompt
from boterview.services.configuration.configuration import Configuration


# The `Boterview` class for conducting up AI-based interview studies.
class Boterview:
    # The `Study` object.
    study: Study

    # Read the participation codes from file.
    def _parse_codes(self: "Boterview", file: str) -> List[Code]:
        """
        Read the codes from a file and return them as a list. Each code is a
        string representing a unique participation code.
        """

        # Open the file.
        with open(file, "r") as f:
            # Get the contents.
            contents = f.read()

        # Split contents by new line.
        codes: List[str] = contents.split("\n")

        # Exclude empty lines.
        codes = [code for code in codes if code]

        # Remove leading and trailing whitespace.
        codes = [code.strip() for code in codes]

        # Initialize the list of codes.
        code_objects: List[Code] = []

        # For each code.
        for code in codes:
            # Initialize the code object.
            code_object: Code = Code(code)

            # Append the code to the list of codes.
            code_objects.append(code_object)

        # Return the list of codes.
        return code_objects

    # Initialize the `Boterview` object.
    def __init__(self: "Boterview") -> None:
        # Create a `Study` object.
        self.study = Study()

    # Prepare the study based on the configuration.
    def initialize_study(self: "Boterview", configuration: Configuration) -> None:
        # Set the study name.
        self.study.set_name(configuration.data["study"]["name"])

        # Parse the study codes.
        codes: List[Code] = self._parse_codes(configuration.data["study"]["codes"])

        # Set the study participation codes.
        self.study.set_codes(codes)

        # For each condition in the configuration.
        for condition in configuration.data["study"]["conditions"]:
            # Create an interview object.
            interview: Interview = Interview()

            # Create an interview `Guide` object.
            interview_guide: Guide = Guide(condition["guide"])

            # Create an interview `Introduction` object.
            interview_introduction: Introduction = Introduction(condition["introduction"])

            # Create an interview `Closing` object.
            interview_closing: Closing = Closing(condition["closing"])

            # Create an interview `Protocol` object.
            interview_protocol: Protocol = Protocol(condition["protocol"])

            # Set the guide.
            interview.set_guide(interview_guide)

            # Set the introduction.
            interview.set_introduction(interview_introduction)

            # Set the closing.
            interview.set_closing(interview_closing)

            # Set the protocol.
            interview.set_protocol(interview_protocol)

            # Create a `Prompt` object.
            model_prompt: Prompt = Prompt(condition["prompt"])

            # Create a condition object.
            condition = Condition(condition["name"], model_prompt, interview)

            # Append the condition to the study.
            self.study.append_condition(condition)

    # Assign a participant to a study condition.
    def assign_participant(self: "Boterview", code: str) -> None:
        # Get the participant.
        participant: Participant | None = self.study.get_participant(code)

        # If the participant is already assigned.
        if participant is not None:
            # Return.
            return None

        # Otherwise, create a new participant.
        participant = Participant(code)

        # Assign the participant to a condition.
        self.study.assign_participant(participant)

    # Retrieve the participant based on the `chainlit` session user identifier.
    def retrieve_participant(self: "Boterview", code: str) -> Participant:
        # Get the participant.
        participant: Participant | None = self.study.get_participant(code)

        # If no participant is found, raise an error.
        if not participant:
            # Throw.
            raise ValueError(f"Could not find an assigned participant with code \"{code}\".")

        # Return the participant.
        return participant

    # Validate a participation code.
    def validate_code(self: "Boterview", code: str) -> bool:
        # Find the code.
        code_object: Code | None = next(
            (c for c in self.study.codes if c.value == code), None
        )

        # Fail if the code is not found or is already used.
        if code_object is None or code_object.used:
            return False

        # Otherwise, mark the code as used.
        code_object.used = True

        # Return success.
        return True

    # Preview a condition in text format.
    def preview_condition(self: "Boterview", name: str) -> None:
        # Attempt to get the condition by name.
        condition: Condition | None = self.study.conditions.get(name)

        # If the condition is not found, raise an error.
        if condition is None:
            raise ValueError(f"Condition \"{name}\" not found for study \"{self.study.name}\".")

        # Get the condition as text.
        text: str = condition.to_text()

        # Print the text.
        print(text)
