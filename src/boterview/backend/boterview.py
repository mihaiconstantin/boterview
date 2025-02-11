# The `Boterview` class for setting up AI-based interview studies.
from .study import Study
from .protocol import Protocol
from .introduction import Introduction
from .closing import Closing
from .guide import Guide
from .interview import Interview
from .condition import Condition
from .prompt import Prompt


class Boterview:
    # The `Study` object.
    study: Study

    # Initialize the `Boterview` object.
    def __init__(self: "Boterview") -> None:
        # Create a new study object.
        self.study = Study()

    # Set the name of the study.
    def set_study_name(self: "Boterview", name: str) -> None:
        # Set the name of the study.
        self.study.name = name

    # Set a study condition.
    def set_study_condition(self: "Boterview", name: str, prompt: str, protocol: str, introduction: str, closing: str, guide: str) -> None:
        # Create an interview `Protocol` object.
        interview_protocol: Protocol = Protocol(protocol)

        # Create an interview `Introduction` object.
        interview_introduction: Introduction = Introduction(introduction)

        # Create an interview `Closing` object.
        interview_closing: Closing = Closing(closing)

        # Create an interview `Guide` object.
        interview_guide: Guide = Guide(guide)

        # Create an interview object.
        interview: Interview = Interview()

        # Set the parts.
        interview.set_protocol(interview_protocol)
        interview.set_introduction(interview_introduction)
        interview.set_closing(interview_closing)
        interview.set_guide(interview_guide)

        # Create a `Prompt` object.
        model_prompt: Prompt = Prompt(prompt)

        # Create a condition object.
        condition = Condition(name, model_prompt, interview)

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
