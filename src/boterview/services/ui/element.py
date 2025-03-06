# Imports.
from typing import Any, Dict, List, Protocol


# The `Element` interface to represent content in the user interface.
class Element(Protocol):
    # Optional element heading.
    heading: str | None

    # Element content.
    content: str | List[str]

    # Metadata.
    metadata: Dict[str, Any]

    # Parse `HTML` content.
    def parse_html(self: "Element", file: str) -> str:
        ...

    # Parse markdown content.
    def parse_markdown(self: "Element", file: str) -> List[str]:
        ...
