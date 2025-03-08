# Imports.
from typing import List
from boterview.services.boterview.printable import Printable
from boterview.services.boterview.protocol import Protocol
from boterview.services.boterview.guide import Guide
from boterview.services.boterview.introduction import Introduction
from boterview.services.boterview.closing import Closing


# `Interview` class.
class Interview(Printable):
    # The interview protocol.
    protocol: Protocol

    # The interview guide.
    guide: Guide

    # The interview introduction.
    introduction: Introduction

    # The interview closing.
    closing: Closing

    # Set the protocol.
    def set_protocol(self: "Interview", protocol: Protocol) -> None:
        # Set.
        self.protocol = protocol

    # Set the guide.
    def set_guide(self: "Interview", guide: Guide) -> None:
        # Set.
        self.guide = guide

    # Set the introduction.
    def set_introduction(self: "Interview", introduction: Introduction) -> None:
        # Set.
        self.introduction = introduction

    # Set the closing.
    def set_closing(self: "Interview", closing: Closing) -> None:
        # Set.
        self.closing = closing

    # Render the interview as text.
    def to_text(self: "Interview") -> str:
        # Collect the parts of the interview in the order they should appear.
        parts = [
            # The guide.
            self.guide.to_text(),

            # The introduction.
            self.introduction.to_text(),

            # The closing.
            self.closing.to_text(),

            # The protocol.
            self.protocol.to_text()
        ]

        # Include the parts that are not empty in the output.
        present_parts: List[str] = [part for part in parts if part != ""]

        # Prepare the output text.
        output: str = "# Interview Document\n\n"

        # Add the parts to the output.
        output += "\n\n".join(present_parts) + "\n"

        # Return the string.
        return output
