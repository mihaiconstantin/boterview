# Imports.
from typing import Any, Dict, List
import pathlib
import copy

# Import content.
from boterview.context.content import TEMPLATE

# Helpers.
from boterview.helpers import utils


# Define a template class.
class Template:
    # The template content.
    content: Dict[str, Any] = TEMPLATE

    # List of configuration keys that refer to files.
    files: List[str] = []

    # Recursively generate a `TOML` string from the configuration template.
    def _parse_template_to_toml(self: "Template", config: Dict[str, Any], parent: str, *, directory: pathlib.Path, secret: bool) -> str:
        # Define commonly used strings.
        new_line: str = "\n"
        empty_line: str = "\n\n"

        # Initialize the text.
        toml: str = ""

        # For each key and item in the template.
        for key, entry in config.items():
            # Get the comment.
            comment: str = entry.get("comment")

            # Get the value.
            value: Dict[str, Any] = entry.get("value")

            # If the value is a dictionary.
            if isinstance(value, dict):
                # Define the name.
                section_name: str = f"{parent}.{key}" if parent else key

                # If we are dealing with conditions.
                if key == "conditions":
                    # Format the section name as an array.
                    section_name = f"[{section_name}]"

                # Write the comment with the right kind of spacing.
                toml += (new_line if parent else empty_line) + f"# {comment}" + new_line

                # Write the name.
                toml += f"[{section_name}]" + new_line

                # Recursively call the function.
                toml += self._parse_template_to_toml(
                    config = value,
                    parent = section_name,
                    directory = directory,
                    secret = secret
                )

            # Otherwise, the value is a string, not a dictionary.
            else:
                # Write the comment.
                toml += f"# {comment}" + new_line

                # If the key represents the `secret_key` and a secret is requested.
                if key == "secret_key" and secret:
                    # Generate a secret.
                    value = utils.generate_secret()

                # If the key is in the list of files.
                if key in self.files:
                    # Write the file path.
                    value = (directory / value).as_posix()

                # If the value is a string.
                if isinstance(value, str):
                    # Wrap it with double quotes.
                    value = f"\"{value}\""

                # If the value is a boolean.
                if isinstance(value, bool):
                    # Convert it to a `TOML` boolean.
                    value = "true" if value else "false"

                # Write the value.
                toml += f"{key} = {value}" + new_line

        # Return the string.
        return toml

    # Get a setting from the configuration template (e.g., `app.secret_key`).
    def get(self: "Template", setting: str, what: str = "value") -> Dict[str, Any] | ValueError:
        """
        Retrieves a configuration setting from an arbitrarily nested template.
        The template is assumed to have keys for both "comment" and "value", where
        nested configurations are stored inside the "value" key.
        """

        # Allowed return elements.
        allowed = ["value", "comment"]

        # If the element to return is not "value" or "comment".
        if what not in allowed:
            # Raise an error.
            raise ValueError(f"Invalid setting element to return. Argument \"what\" must be one of {utils.list_to_enumeration(allowed, "or")}.")

        # Split the setting path into parts.
        parts = setting.split(".")

        # Start at the root of the template.
        result = self.content

        # Define the error.
        ERROR = 'Setting "{}" in "{}" not found in the configuration template.'

        # For each part of the setting path.
        for part in parts:

            # If the current part is a key in the tree.
            if isinstance(result, dict) and part in result:
                # Move to the next part.
                result = result[part]

            # Otherwise, if the current part is a dictionary with a "value" key.
            elif isinstance(result, dict) and "value" in result:
                # Move to the "value" key.
                nested = result["value"]

                # If the part is a key in the nested dictionary.
                if isinstance(nested, dict) and part in nested:
                    # Move to the next part.
                    result = nested[part]

                # Otherwise, the key is not present.
                else:
                    # Raise an error.
                    raise ValueError(ERROR.format(part, setting))

            # Otherwise, the key is not present
            else:
                # Raise an error.
                raise ValueError(ERROR.format(part, setting))

        # If the result is a dictionary with the correct keys.
        if isinstance(result, dict) and "comment" in result and "value" in result:
            # Return the requested element for the setting.
            return copy.deepcopy(result[what])

        # Otherwise, the setting is improperly formatted in the template.
        else:
            # Raise an error.
            raise ValueError(f"Setting \"{setting}\" is not properly structured in the template.")

    # Print the configuration template to text.
    def to_toml(self: "Template", directory: pathlib.Path, secret: bool) -> str:
        # Initialize the text.
        toml: str = "# Configuration file for the `boterview` application."

        # Parse the configuration template.
        toml += self._parse_template_to_toml(
            config = self.content,
            parent = "",
            directory = directory,
            secret = secret
        )

        # Return the `TOML` string.
        return toml
