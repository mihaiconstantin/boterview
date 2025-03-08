# Imports.
from typing import List
import pathlib
import click
from boterview.services.configuration.configuration import Configuration

# Import the content.
from boterview.context.content import CONTENT

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


# Subcommand for an example study setup.
@generate.command(name = "study")
@click.option("-p", "--path", type = str, required = True, help = "The path where to scaffold the study setup.")
@click.option("-q", "--quantity", type = int, required = True, help = "The amount of participation codes to generate.")
@click.option("-c", "--config", type = str, required = False, default = "study.toml", help = "The name of the configuration file.")
@click.option("-s", "--secret", is_flag = True, help = "Whether to include a secret in the configuration file.")
def study(path: str, quantity: int, config: str, secret: bool):
    """Command to scaffold an example study setup at the path provided."""

    # Define the the scaffolding location.
    location: pathlib.Path = pathlib.Path(path)

    # Create a configuration instance.
    configuration: Configuration = Configuration()

    # Write the configuration file.
    utils.create_and_write_contents(
        file = location / f"{config}",
        contents = configuration.template.to_toml(
            directory = location,
            secret = secret
        )
    )

    # Prepare the list of files to write.
    configuration_files = {
        # The UI files.
        "ui": {key for key in configuration.configuration_format["ui"]},

       # The study files.
        "study": {
            "codes": {},
            "conditions": {key for key in configuration.configuration_format["study"]["conditions"] if key != "name"}
        }
    }

    # For each section that has files to be written.
    for section in configuration_files:

        # For setting in the respective section.
        for setting in configuration_files[section]:

            # If we are dealing with UI files.
            if section == "ui":
                # Determine the path to write at.
                file = location / f"{configuration.template.get(f"{section}.{setting}.content")}"

                # Determine the content.
                contents = str(CONTENT[section][setting])

                # Write the file.
                utils.create_and_write_contents(file, contents)

                # Continue to the next iteration.
                continue

            # If we are dealing with study files.
            if section == "study":
                # If we are dealing with condition files.
                if setting == "conditions":
                    # For each condition.
                    for condition in configuration_files[section][setting]:
                        # Determine the path to write at.
                        file = location / f"{configuration.template.get(f"{section}.{setting}.{condition}")}"

                        # Determine the content.
                        contents = CONTENT[section][setting][condition]

                        # Write the file.
                        utils.create_and_write_contents(file, contents)

                # Otherwise, it's a study-level file.
                else:
                    # Determine the path to write at.
                    file = location / f"{configuration.template.get(f"{section}.{setting}")}"

                    # If the setting is codes, generate the codes.
                    if setting == "codes":
                        # Generate the codes.
                        contents = "\n".join(utils.generate_codes(quantity))

                    # Otherwise, get the content from the default contents.
                    else:
                        contents = str(CONTENT[section][setting])

                    # Write the file.
                    utils.create_and_write_contents(file, contents)

    # User feedback.
    click.echo(f"Study setup scaffolded. The configuration file is available at \"{location / config}\".")
