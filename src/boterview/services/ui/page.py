# Imports.
from typing import Any, Dict, List
from boterview.services.ui.element import Element

# Helpers.
import boterview.helpers.utils as utils


# The `Page` class to represent page content in the user interface.
class Page(Element):
    # Page heading.
    heading: str | None

    # Page content.
    content: str

    # Metadata.
    metadata: Dict[str, Any] = {}

    # Parse `HTML` content.
    def parse_html(self: "Page", file: str) -> str:
        # Read the file contents.
        contents: str = utils.read_contents(file)

        # Return the contents trimmed.
        return contents.strip()

    # Parse markdown content.
    def parse_markdown(self: "Page", file: str) -> str:
        # Read the file contents.
        contents: str = utils.read_contents(file)

        # Return the chunks.
        return contents.strip()

    # Initialize the `Page` object.
    def __init__(self: "Page", heading: str, file: str, metadata: Dict[str, Any]) -> None:
        # Set the page heading.
        self.heading = heading

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
