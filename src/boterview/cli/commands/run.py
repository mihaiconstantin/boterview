# Imports.
import click


# Command to run a `boterview` study.
@click.command(name = "run")
@click.option("--config", type = str, required = True, help = "The study `.toml` configuration file to use.")
def run(config: str):
    """Run a `boterview` study using a provided configuration file."""
    print("Work in progress...")
