# Imports.
from typing import Any, Dict
import os
import tomllib
import dotenv
from boterview.services.configuration.template import Template

# Helpers.
from boterview.helpers import utils


# `Configuration` class.
class Configuration:
    # The configuration template with sensible defaults.
    template: Template

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
            "initial_message": str | None,
            "resume_message": str | None
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

    # Load the `.env` file.
    def _load_env_file(self: "Configuration") -> None:
        # Find the `.env` file.
        env_file = dotenv.find_dotenv()

        # If the file exists.
        if env_file:
            # Load the `.env` file.
            dotenv.load_dotenv(env_file)

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

    # Set optional keys to null if values are not provided.
    def _validate_configuration_format(self: "Configuration") -> None:
        # For each configuration section in the expected format.
        for section, section_type in self.configuration_sections.items():

            # If the section is optional and not provided in the configuration file.
            if utils.is_optional(section_type) and section not in self.data:
                # Set the section to an empty dictionary.
                self.data[section] = {}

            # For each key in the current section.
            for key, key_type in self.configuration_format[section].items():

                # If the key is optional and not provided in the configuration file.
                if utils.is_optional(key_type) and key not in self.data[section]:
                    # If the type is a dictionary.
                    if utils.is_dictionary(key_type):
                        # Set the key to an empty dictionary.
                        self.data[section][key] = {}
                    else:
                        # Set the key to `None`.
                        self.data[section][key] = None

                # Assert that the key is present in the parsed configuration.
                assert key in self.data[section], f"Missing configuration key \"{ section }.{ key }\"."

                # If the key belongs to the conditions list.
                if key == "conditions":

                    # For each condition provided in the configuration.
                    for condition in self.data[section][key]:

                        # For each condition key in the conditions list of keys.
                        for condition_key, condition_key_type in self.configuration_format[section][key].items():

                            # If the key is optional and not provided in the configuration file for the current condition.
                            if utils.is_optional(condition_key_type) and condition_key not in condition:
                                # Set the key to `None`.
                                condition[condition_key] = None

                            # Assert that the condition key is present in the current condition.
                            assert condition_key in condition, f"Missing configuration key \"{ section }.{ key }.{ condition_key }\"."

                # If the key belongs to the `ui` dictionary.
                if key in self.configuration_format["ui"].keys() and not utils.is_optional(key_type):

                    # For each `ui` key in the expected format.
                    for ui_key, ui_key_type in self.configuration_format[section][key].items():

                        # If the key is optional and not provided in the configuration file.
                        if utils.is_optional(ui_key_type) and ui_key not in self.data[section][key]:
                            # Set the key to `None`.
                            self.data[section][key][ui_key] = None

                        # Assert that the `ui` key is present in the parsed configuration.
                        assert ui_key in self.data[section][key], f"Missing configuration key \"{ section }.{ key }.{ ui_key }\"."

    # Parse the bot `API` key.
    def _parse_api_key(self: "Configuration") -> None:
        # Try to get the key in case the user provided it as an environment variable.
        api_key: str = os.environ.get(self.data["bot"]["api_key"], self.data["bot"]["api_key"])

        # Update the `API` key entry in the configuration.
        self.data["bot"]["api_key"] = api_key

    # Parse the application secret key.
    def _parse_secret_key(self: "Configuration") -> None:
        # Try to get the key in case the user provided it as an environment variable.
        app_secret: str = os.environ.get(self.data["app"]["secret_key"], self.data["app"]["secret_key"])

        # If the secret is not long enough.
        if len(app_secret) < 20:
            # Raise an error.
            raise ValueError("The secret key is too short. Run `boterview generate secret` to generate a proper random secret key.")

        # Update the secret key entry in the configuration.
        self.data["app"]["secret_key"] = app_secret

    # Set default values for optional keys.
    def _set_default_values(self: "Configuration") -> None:
        # Set default values for the `bot` section.
        self.data["bot"]["settings"]["model"] = self.data["bot"]["settings"].get("model", self.template.get("bot.settings.model"))

        # Set default values for the `chat` section.
        self.data["chat"]["stop_response_bot_triggered"] = self.data["chat"]["stop_response_bot_triggered"] or self.template.get("chat.stop_response_bot_triggered")
        self.data["chat"]["stop_response_user_triggered"] = self.data["chat"]["stop_response_user_triggered"] or self.template.get("chat.stop_response_user_triggered")
        self.data["chat"]["stop_button_label"] = self.data["chat"]["stop_button_label"] or self.template.get("chat.stop_button_label")
        self.data["chat"]["initial_message"] = self.data["chat"]["initial_message"] or self.template.get("chat.initial_message")
        self.data["chat"]["resume_message"] = self.data["chat"]["resume_message"] or self.template.get("chat.resume_message")

        # Set default values for the `study` section.
        self.data["study"]["name"] = self.data["study"]["name"] or self.template.get("study.name")
        self.data["study"]["protocol_process"] = self.data["study"]["protocol_process"] or self.template.get("study.protocol_process")
        self.data["study"]["protocol_question_separator"] = self.data["study"]["protocol_question_separator"] or self.template.get("study.protocol_question_separator")

        # Set default values for the `ui` section.
        self.data["ui"]["welcome"]["html"] = self.data["ui"]["welcome"]["html"] or self.template.get("ui.welcome.html")
        self.data["ui"]["consent"]["html"] = self.data["ui"]["consent"]["html"] or self.template.get("ui.consent.html")
        self.data["ui"]["stop"]["html"] = self.data["ui"]["stop"]["html"] or self.template.get("ui.stop.html")
        self.data["ui"]["stop"]["timeout"] = self.data["ui"]["stop"]["timeout"] if self.data["ui"]["stop"]["timeout"] is not None else self.template.get("ui.stop.timeout")

        # Special case for the `footer` dictionary.
        self.data["ui"]["footer"]["content"] = self.data["ui"]["footer"].get("content", None)
        self.data["ui"]["footer"]["html"] = self.data["ui"]["footer"].get("html", None)

    # Set the template.
    def _set_template(self: "Configuration") -> None:
        # Initialize the configuration template.
        self.template = Template()

        # Set the template keys that refer to files.
        self.template.files = [
            "content",
            "codes"
        ] + [key for key in self.configuration_format["study"]["conditions"] if key != "name"]

    # Initialize the configuration.
    def __init__(self: "Configuration") -> None:
        # Set the template.
        self._set_template()

        # Initialize the configuration data.
        self.data = {}

    # Initialize the configuration.
    def load_configuration(self: "Configuration", config_file: str) -> None:
        # Load the `.env` file.
        self._load_env_file()

        # Read the `TOML` config from a file.
        with open(config_file, "rb") as file:
            # Parse the file as a dictionary.
            self.data = tomllib.load(file)

        # Validate the required configuration keys.
        self._validate_configuration_sections()

        # Validate the required configuration format.
        self._validate_configuration_format()

        # Parse the bot `API` key.
        self._parse_api_key()

        # Parse the secret key.
        self._parse_secret_key()

        # Set default values for optional keys.
        self._set_default_values()
