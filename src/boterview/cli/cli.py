# Imports.
import click
import sys

# Import the commands.
from boterview.cli.commands.preview import preview
from boterview.cli.commands.run import run
from boterview.cli.commands.generate import generate

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

if __name__ == "__main__":
    cli()
