# Imports.
from datetime import datetime, timezone
import click
from boterview.services.configuration.configuration import Configuration
from boterview.services.boterview.boterview import Boterview

# Helpers.
import boterview.helpers.storage as storage
import boterview.helpers.utils as utils

# Import the context.
import boterview.context.app as app
import boterview.context.persistence as persistence


# Command to parse the database as a `markdown` file.
@click.command(name = "parse")
@click.option("-c", "--config", type = str, required = True, help = "The study `.toml` configuration file used.")
@click.option("-d", "--database", type = str, required = True, help = "The database file to parse.")
def parse(config: str, database: str):
    """
    Command to parse the study database. You can also navigate to the
    `/downloads` route in the application to download the parsed database via
    the application interface. The later assumes the application is still
    running.
    """

    # Get the current configuration.
    configuration: Configuration = app.get_configuration()

    #  Get the current `boterview` instance.
    boterview: Boterview = app.get_boterview()

    # Load the configuration.
    configuration.load_configuration(config)

    # Initialize the `boterview` study.
    boterview.initialize_study(configuration)

    # Initialize the database.
    persistence.initialize_database(database)

    # Parse the database.
    contents: str = storage.parse_database(boterview)

    # Close the database connection.
    persistence.database.close()

    # Prepare the file name.
    output_file: str = f"output-{configuration.data["study"]["name"].lower().replace(" ", "-")}-{datetime.now(timezone.utc).strftime("%Y-%m-%d-%H-%M-%S")}.md"

    # Write contents to a file.
    utils.write_contents(output_file, contents)

    # User feedback.
    click.echo(f"Database parsed successfully. The output file is available at \"{output_file}\".")
