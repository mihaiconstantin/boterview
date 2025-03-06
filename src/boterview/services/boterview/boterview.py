# Imports.
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
    # The `Configuration` object.
    configuration: Configuration

    # The `Study` object.
    study: Study

    # Initialize the `Boterview` object.
    def __init__(self: "Boterview", configuration: str) -> None:
        # Parse the configuration file.
        self.configuration = Configuration(configuration)

        # Create a `Study` object.
        self.study = Study()

    # Prepare the study based on a `Configuration` object.
    def initialize_study(self: "Boterview") -> None:
        # Set the study name.
        self.study.set_name(self.configuration.data["study"]["name"])

        # For each condition in the configuration.
        for condition in self.configuration.data["study"]["conditions"]:
            # Create an interview `Protocol` object.
            interview_protocol: Protocol = Protocol(condition["protocol"])

            # Create an interview `Introduction` object.
            interview_introduction: Introduction = Introduction(condition["introduction"])

            # Create an interview `Closing` object.
            interview_closing: Closing = Closing(condition["closing"])

            # Create an interview `Guide` object.
            interview_guide: Guide = Guide(condition["guide"])

            # Create an interview object.
            interview: Interview = Interview()

            # Set the parts.
            interview.set_protocol(interview_protocol)
            interview.set_introduction(interview_introduction)
            interview.set_closing(interview_closing)
            interview.set_guide(interview_guide)

            # Create a `Prompt` object.
            model_prompt: Prompt = Prompt(condition["prompt"])

            # Create a condition object.
            condition = Condition(condition["name"], model_prompt, interview)

            # Append the condition to the study.
            self.study.append_condition(condition)

    # Preview a condition in text format.
    def preview_condition(self: "Boterview", name: str) -> None:
        # Attempt to get the condition by name.
        condition: Condition | None = self.study.conditions.get(name)

        # If the condition is not found, raise an error.
        if condition is None:
            raise ValueError(f"Condition '{name}' not found for study '{self.study.name}'.")

        # Merge the text.
        text: str = condition.prompt.text

        # Add an empty line.
        text += "\n\n"

        # Add the protocol.
        text += condition.interview.to_text()

        # Print the text.
        print(text)
