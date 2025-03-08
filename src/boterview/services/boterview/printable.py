# Imports.
from abc import ABC, abstractmethod


# Define the `Printable` interface for print-like functionality.
class Printable(ABC):
    # Print an object to readable format (i.e., as string).
    @abstractmethod
    def to_text(self: "Printable") -> str:
        pass
