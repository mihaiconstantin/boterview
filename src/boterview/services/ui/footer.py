# Imports.
from typing import Any, Dict, List
from boterview.services.ui.element import Element

# Helpers.
import boterview.helpers.utils as utils


# The `Footer` class to represent a page footer in the user interface.
class Footer(Element):
    # Footer heading.
    heading: str | None = None

    # Footer content.
    content: str | List[str]

    # Metadata.
    metadata: Dict[str, Any] = {}

    # Parse `HTML` content.
    def parse_html(self: "Footer", file: str) -> str:
        # Read the file contents.
        contents: str = utils.read_contents(file)

        # Return the contents trimmed.
        return contents.strip()

    # Parse markdown content.
    def parse_markdown(self: "Footer", file: str) -> List[str]:
        # Read the file contents.
        contents: str = utils.read_contents(file)

        # Set the chunks.
        chunks: List[str] = contents.split("\n\n")

        # Trim the chunks.
        chunks = [chunk.strip() for chunk in chunks]

        # Return the chunks.
        return chunks

    # Initialize the `Footer` object.
    def __init__(self: "Footer", file: str, metadata: Dict[str, Any]) -> None:
        # If the content is provided as `HTML`.
        if metadata.get("html", False):
            # Set the content as the `HTML`.
            self.content = self.parse_html(file)

        # Otherwise parse the content as markdown paragraph chunks.
        else:
            # Set the content as chunks.
            self.content = self.parse_markdown(file)

        # Set the metadata.
        self.metadata = metadata
