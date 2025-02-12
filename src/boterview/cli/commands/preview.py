# Imports.
import click
from boterview.backend.boterview import Boterview


# Command to preview study-related content.
@click.command(name = "preview")
@click.option("--config", type = str, required = True, help = "The study `.toml` configuration file to use.")
@click.option("--condition", type = str, required = True, help = "The condition to preview.")
def preview(config: str, condition: str):
    """Preview preview the interview for a configured condition."""

    # Create the `Boterview` object.
    boterview: Boterview = Boterview(config)

    # Initialize the study.
    boterview.initialize_study()

    # Preview the condition.
    boterview.preview_condition(name = condition)
