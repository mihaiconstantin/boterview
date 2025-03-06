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
