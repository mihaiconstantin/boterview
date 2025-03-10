# Imports.
import pathlib
from importlib import resources


# The package source directory.
_PACKAGE_SOURCE: pathlib.Path | None = None

#  The package root directory.
_PACKAGE_ROOT: pathlib.Path | None = None


# Initialize the package paths.
def initialize_package_paths() -> None:
    """Initialize the package paths."""

    # Access the global package paths.
    global _PACKAGE_ROOT, _PACKAGE_SOURCE

    # Extract the package source
    _PACKAGE_SOURCE = pathlib.Path(str(resources.files("boterview"))).resolve()

    # If we are in development mode.
    if _PACKAGE_SOURCE.parts[-2:] == ("src", "boterview"):
        # Compute the root manually.
        _PACKAGE_ROOT = _PACKAGE_SOURCE.parents[1]

    # Otherwise, we are in production mode.
    else:
        # Compute the root using the resources module.
        _PACKAGE_ROOT = _PACKAGE_SOURCE


# Get package source directory.
def get_package_source() -> pathlib.Path:
    """Get the package source directory."""

    # Ensure the package source is initialized.
    if _PACKAGE_SOURCE is None:
        # Initialize the package paths.
        initialize_package_paths()

    # Assert the package source is not `None`.
    assert _PACKAGE_SOURCE is not None, "Package source directory not initialized."

    # Return the package source directory.
    return _PACKAGE_SOURCE


# Get the package root directory.
def get_package_root() -> pathlib.Path:
    """Get the package root directory."""

    # Ensure the package root is initialized.
    if _PACKAGE_ROOT is None:
        # Initialize the package paths.
        initialize_package_paths()

    # Assert the package root is not `None`.
    assert _PACKAGE_ROOT is not None, "Package root directory not initialized."

    # Return the package root directory.
    return _PACKAGE_ROOT
