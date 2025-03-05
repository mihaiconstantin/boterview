# Imports.
import os
import tomllib
from typing import Any, Dict, List


# `Configuration` class.
class Configuration:
    # The configuration.
    data: Dict[str, Any]

    # Define the required config keys.
    configuration_keys: List[str] = ["bot", "study"]

    # Expected configuration format.
    configuration_format: Dict[str, Any] = {
        "bot": {
            "api_key": str,
            "model": str,
        },
        "study": {
            "name": str,
            "conditions": {
                "name": str,
                "prompt": str,
                "protocol": str,
                "introduction": str,
                "closing": str,
                "guide": str
            }
        }
    }

    # Check that required configuration keys are present.
    def _validate_configuration_keys(self: "Configuration") -> None:
        # For each key.
        for key in self.configuration_keys:
            # Check if it is present.
            assert key in self.data, f"Missing configuration section '{ key }'."

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
