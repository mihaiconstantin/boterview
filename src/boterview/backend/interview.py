# Imports.
from .printable import Printable
from .protocol import Protocol
from .guide import Guide
from .introduction import Introduction
from .closing import Closing


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
        # Prepare the output text.
        output: str = "# Interview Document\n\n"

        # Add the guide.
        output += self.guide.to_text() + "\n\n"

        # Add the protocol.
        output += self.introduction.to_text() + "\n\n"

        # Add the closing.
        output += self.closing.to_text() + "\n\n"

        # Add the protocol.
        output += self.protocol.to_text() + "\n"

        # Return the string.
        return output
