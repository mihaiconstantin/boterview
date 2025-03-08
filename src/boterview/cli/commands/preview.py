# Imports.
import click
from boterview.services.configuration.configuration import Configuration
from boterview.services.boterview.boterview import Boterview

# Import application context.
import boterview.context.app as app


# Command to preview study-related content.
@click.command(name = "preview")
@click.option("-c", "--config", type = str, required = True, help = "The study `.toml` configuration file to use.")
@click.option("--condition", type = str, required = True, help = "The condition to preview.")
def preview(config: str, condition: str):
    """Command to preview a study condition given a configuration file."""

    # Create a configuration object.
    configuration: Configuration = app.get_configuration()

    # Load the configuration.
    configuration.load_configuration(config)

    # Create the `Boterview` object.
    boterview: Boterview = app.get_boterview()

    # Initialize the study.
    boterview.initialize_study(configuration)

    # Preview the condition.
    boterview.preview_condition(name = condition)
