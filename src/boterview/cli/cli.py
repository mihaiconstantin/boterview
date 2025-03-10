# Imports.
import click
import sys

# Import the commands.
from boterview.cli.commands.preview import preview
from boterview.cli.commands.run import run
from boterview.cli.commands.generate import generate
from boterview.cli.commands.parse import parse


# Disable traceback.
sys.tracebacklimit = 0


# Main CLI group for the application commands.
@click.group()
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
