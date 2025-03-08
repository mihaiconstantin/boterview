# Imports.
from boterview.services.configuration.configuration import Configuration
from boterview.services.ui.ui import UI
from boterview.services.boterview.boterview import Boterview


# The `Configuration` instance.
_configuration: Configuration | None = None

# Create a `UI` instance.
_ui: UI | None = None

# Create a `Boterview` instance.
_boterview: Boterview | None = None


# Define an application factory function.
def create_application() -> tuple[Configuration, UI, Boterview]:
    # Create a new `Configuration` instance.
    configuration: Configuration = Configuration()

    # Create a new `UI` instance.
    ui: UI = UI()

    # Create a new `Boterview` instance.
    boterview: Boterview = Boterview()

    # Return the application instances.
    return configuration, ui, boterview


# Initialize the `boterview` application.
def initialize_application() -> None:
    # Access the global variables.
    global _configuration, _ui, _boterview

    # If the application instances are not yet initialized.
    if _configuration is None or _ui is None or _boterview is None:
        # Create the application instances.
        _configuration, _ui, _boterview = create_application()


# Get the `Configuration` instance.
def get_configuration() -> Configuration:
    # Ensure the configuration is initialized.
    if _configuration is None:
        # Initialize the application.
        initialize_application()

    # Assert the configuration is not `None`.
    assert _configuration is not None, "`Configuration` instance not initialized."

    # Return the configuration.
    return _configuration


# Get the `UI` instance.
def get_ui() -> UI:
    # Ensure the UI is initialized.
    if _ui is None:
        # Initialize the application.
        initialize_application()

    # Assert the UI is not `None`.
    assert _ui is not None, "`UI` instance not initialized."

    # Return the UI.
    return _ui


# Get the `Boterview` instance.
def get_boterview() -> Boterview:
    # Ensure the `Boterview` is initialized.
    if _boterview is None:
        # Initialize the application.
        initialize_application()

    # Assert the `Boterview` is not `None`.
    assert _boterview is not None, "`Boterview` instance not initialized."

    # Return the `Boterview`.
    return _boterview
