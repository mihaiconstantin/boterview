# Imports.
from typing import Any, Dict
import os
import tomllib

# Helpers.
from boterview.helpers import utils


# `Configuration` class.
class Configuration:
    # The configuration.
    data: Dict[str, Any]

    # Define the config keys.
    configuration_sections: Dict[str, Any] = {
        "app": Any,
        "bot": Any,
        "ui": Any,
        "chat": Any | None,
        "study": Any
    }

    # Expected configuration format.
    configuration_format: Dict[str, Any] = {
        "app": {
            "secret_key": str
        },
        "bot": {
            "api_key": str,
            "settings": Dict[str, Any] | None,
        },
        "ui": {
            "welcome": {
                "heading": str,
                "content": str,
                "html": bool | None
            },
            "consent": {
                "heading": str,
                "content": str,
                "html": bool | None
            },
            "stop": {
                "heading": str,
                "content": str,
                "html": bool | None,
                "timeout": int | None
            },
            "footer": Dict[str, Any] | None
        },
        "chat": {
            "stop_response_bot_triggered": str | None,
            "stop_response_user_triggered": str | None,
            "stop_button_label": str | None,
            "initial_message": str | None
        },
        "study": {
            "name": str | None,
            "codes": str,
            "protocol_process": bool | None,
            "protocol_question_separator": str | None,
            "conditions": {
                "name": str,
                "prompt": str,
                "protocol": str,
                "guide": str | None,
                "introduction": str | None,
                "closing": str | None
            }
        }
    }


    # Check that required configuration sections are present.
    def _validate_configuration_sections(self: "Configuration") -> None:
        # For each key.
        for section, section_type in self.configuration_sections.items():

            # If the key is optional.
            if utils.is_optional(section_type):
                # Skip the check.
                continue

            # Check if it is present.
            assert section in self.data, f"Missing configuration section \"{ section }\"."

    # Check the required configuration format.
    def _validate_configuration_format(self: "Configuration") -> None:
        # For each configuration section in the expected format.
        for section in self.configuration_format:

            # For each expected key in the current section.
            for key in self.configuration_format[section].keys():

                # Assert that the key is present in the parsed configuration.
                assert key in self.data[section], f"Missing configuration key '{ section }.{ key }'."

                # If the key happens to be the `conditions` list.
                if key == "conditions":

                    # For each condition key in the expected format.
                    for condition_key in self.configuration_format[section][key].keys():

                        # Assert that the condition key is present in the parsed configuration for each condition.
                        for condition in self.data[section][key]:

                            # Assert that the condition key is present in the current condition.
                            assert condition_key in condition, f"Missing configuration key '{ section }.{ key }.{ condition_key }'."

    # Parse the `API` key.
    def _parse_api_key(self: "Configuration") -> None:
        # Try to get the key in case the user provided an environment variable.
        api_key: str = os.environ.get(self.data["bot"]["api_key"], self.data["bot"]["api_key"])

        # Update the `API` key entry in the configuration.
        self.data["bot"]["api_key"] = api_key

    # Initialize the configuration.
    def __init__(self: "Configuration", config_file: str) -> None:
        # Read the `TOML` config from a file.
        with open(config_file, "rb") as file:
            # Parse the file as a dictionary.
            self.data = tomllib.load(file)

        # Validate the required configuration keys.
        self._validate_configuration_keys()

        # Validate the required configuration format.
        self._validate_configuration_format()

        # Parse the `API` key.
        self._parse_api_key()
