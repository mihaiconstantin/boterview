# Imports.
import click
import sys

# Helpers.
from boterview.helpers import utils

# Import the commands.
from boterview.cli.commands.preview import preview
from boterview.cli.commands.run import run
from boterview.cli.commands.generate import generate
from boterview.cli.commands.parse import parse


# Disable traceback.
sys.tracebacklimit = 0

# Get the package version message.
message: str = utils.get_package_logo()


# Main CLI group for the application commands.
@click.group()
@click.version_option(package_name = "boterview", message = message)
def cli():
    """`boterview` commands for managing your study."""
    pass

# Add the `preview` command to the group.
cli.add_command(preview)

# Add the `run` command to the group.
cli.add_command(run)

# Add the `generate` command to the group.
cli.add_command(generate)

# Add the `parse` command to the group.
cli.add_command(parse)


# If the script is run directly.
if __name__ == "__main__":
    # Run the CLI.
    cli()
