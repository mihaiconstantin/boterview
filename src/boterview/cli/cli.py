# Imports.
import click
import sys

# Import the commands.
from boterview.cli.commands.preview import preview
from boterview.cli.commands.run import run

# Disable traceback.
sys.tracebacklimit = 0


# The CLI group for the application commands.
@click.group()
def cli():
    """Below you can find the supported `boterview` command line interface (CLI) commands."""
    pass

# Add the `preview` command to the group.
cli.add_command(preview)

# Add the `run` command to the group.
cli.add_command(run)

if __name__ == "__main__":
    cli()
