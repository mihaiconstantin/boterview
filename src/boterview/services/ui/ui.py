# Imports.
from typing import Dict
from boterview.services.configuration.configuration import Configuration
from boterview.services.ui.element import Element
from boterview.services.ui.page import Page
from boterview.services.ui.footer import Footer


# `UI` class for the user interface elements.
class UI:
    # The `UI` elements.
    elements: Dict[str, Element]

    # Initialize the `UI` object.
    def __init__(self: "UI") -> None:
        # Initialize the elements.
        self.elements = {}

    # Get an element from the `UI` object.
    def get_element(self: "UI", key: str) -> Element:
        # Return the element.
        return self.elements[key]

    # Initialize the user interface based on the configuration.
    def initialize_ui(self: "UI", configuration: Configuration) -> None:
        # Add the welcome page element.
        self.elements["welcome"] = Page(
            heading = configuration.data["ui"]["welcome"]["heading"],
            file = configuration.data["ui"]["welcome"]["content"],
            metadata ={
                "html": configuration.data["ui"]["welcome"]["html"]
            }
        )

        # Add the consent page element.
        self.elements["consent"] = Page(
            heading = configuration.data["ui"]["consent"]["heading"],
            file = configuration.data["ui"]["consent"]["content"],
            metadata ={
                "html": configuration.data["ui"]["consent"]["html"]
            }
        )

        # Add the stop page element.
        self.elements["stop"] = Page(
            heading = configuration.data["ui"]["stop"]["heading"],
            file = configuration.data["ui"]["stop"]["content"],
            metadata ={
                "html": configuration.data["ui"]["stop"]["html"],
                "timeout": configuration.data["ui"]["stop"]["timeout"]
            }
        )

        # If the footer element is provided.
        if configuration.data["ui"]["footer"]["content"]:
            # Add it.
            self.elements["footer"] = Footer(
                file = configuration.data["ui"]["footer"]["content"],
                metadata ={
                    "html": configuration.data["ui"]["footer"]["html"]
                }
            )
