# Imports.
from typing import Any, Dict
import copy

# Import content.
from boterview.context.content import TEMPLATE

# Helpers.
from boterview.helpers import utils


# Define a template class.
class Template:
    # The template content.
    content: Dict[str, Any] = TEMPLATE

    # Recursively generate a `TOML` string from the configuration template.

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

