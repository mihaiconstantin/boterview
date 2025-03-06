# Imports.
from typing import List, LiteralString
import pathlib
import os
import secrets
import string


# Parse the contents of a file.
def read_contents(file: str) -> str:
    """
    Read the contents of a file and return them as a string.
    """

    # Open the file.
    with open(file, "r") as f:
        # Read the contents.
        content = f.read()

    # Remove leading and trailing whitespace.
    content = content.strip()

    # Return the contents.
    return content


# Write contents to a file.
def write_contents(file: str | pathlib.Path, contents: str) -> None:
    """
    Write the contents to a file and return the status.
    """

    # Attempt to write the contents to the file.
    try:
        # Write the contents to the file.
        with open(file, "w") as f:
            # Write the contents.
            f.write(contents)

    # If an exception occurs.
    except Exception as e:
        # Throw.
        raise e


# Create file path and write contents to a file.
def create_and_write_contents(file: str | pathlib.Path, contents: str) -> None:
    """
    Create a file and its parent directories, and write the contents to it.
    """

    # Create the file path.
    file = pathlib.Path(file)

    # Create the parents if they don't
    file.parent.mkdir(parents = True, exist_ok = True)

    # Write the contents to the file.
    write_contents(file, contents)


# Generate a random code as a study participation code.
def generate_codes(quantity: int, length: int = 6) -> List[str]:
    # Create a placeholder for the codes.
    codes: List[str] = []

    # Define the allowed characters for the code.
    characters: LiteralString = string.ascii_letters + string.digits

    # Generate the codes.
    for _ in range(quantity):
        # Generate a random code.
        code: str = "".join(secrets.choice(characters) for _ in range(length)).upper()

        # Append the code to the list of codes.
        codes.append(code)

    # Return the list of codes.
    return codes


# Generate a random application secret.
def generate_secret(length: int = 64):
    # Define the allowed characters for the secret.
    chars: LiteralString = string.ascii_letters + string.digits + "$%*,-./:=>?@^_~"

    # Generate a random secret.
    secret: str = "".join(secrets.choice(chars) for _ in range(length))

    # Return the secret.
    return secret


# Get the a variable from the environment.
def get_environment_variable(variable: str) -> str:
    # Get the value of the environment variable.
    value: str | None = os.environ.get(variable)

    # If the value is not available.
    if not value:
        # Raise an exception.
        raise ValueError(f"The environment variable \"{ variable }\" is not available. Please set it.")

    # Return the value of the environment variable.
    return value


# Return a list the human-like enumeration string.
def list_to_enumeration(list: List[str], conjunction: str) -> str:
    # Wrap each element in quotes.
    list = [f"\"{element}\"" for element in list]

    # Output.
    output: str

    # If there are no elements in the list.
    if len(list) == 0:
        # Return an empty string.
        output = ""

        # Return
        return output

    # If there is only one element in the list.
    if len(list) == 1:
        # Return the element.
        output = list[0]

        # Return
        return output

    # If there are two elements in the list.
    if len(list) == 2:
        # Return the elements separated by the preposition.
        output = f" {conjunction} ".join(list)

        # Return
        return output

    # For more than two elements, enumerate and add the preposition.
    output = ", ".join(list[:-1]) + f", {conjunction} " + list[-1]

    # Return the output.
    return output

