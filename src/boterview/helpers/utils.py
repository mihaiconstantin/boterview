# Imports.
import pathlib


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

