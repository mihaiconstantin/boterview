# Imports.
from typing import List
import click

# Import helpers.
import boterview.helpers.utils as utils


# Create a command group for generate.
@click.group()
def generate():
    """Commands to generate various things."""
    pass


# Subcommand for generating participation codes.
@generate.command(name = "codes")
@click.option("-q", "--quantity", type = int, required = True, help = "The amount of participation codes to generate.")
@click.option("-f", "--file", type = str, required = False, help = "The file to write the codes to.")
def codes(quantity: int, file: str):
    """Command to generate participation codes."""

    # Generate six letter codes only from letters and digits.
    codes: List[str] = utils.generate_codes(quantity)

    # Prepare the contents.
    contents: str = "\n".join(codes)

    # If the file is missing, the only print the codes.
    if file is None:
        # Print the codes.
        click.echo(contents)

        # Return.
        return

    # Otherwise, open the file.
    utils.write_contents(file, contents)

    # Print a success message.
    click.echo(f"Generated { quantity } codes written to '{ file }'.")


# Subcommand for generating a random secret.
@generate.command(name = "secret")
def secret():
    """Command to generate a random secret."""

    # Generate a secret.
    secret: str = utils.generate_secret()

    # Print the secret.
    click.echo(
        f"Generated secret: {secret}\n"
        "You may copy this secret to your configuration file."
    )
