# Imports.
import pathlib
from typing import Any, Dict, List
import sys
import shutil
import subprocess
from hatchling.builders.hooks.plugin.interface import BuildHookInterface


# Define a custom exception for build errors.
class BoterviewBuildError(Exception):
    pass


# Define a build hook for building the frontend.
class Frontend(BuildHookInterface):
    # Define the name of the hook.
    PLUGIN_NAME: str = "frontend"

    # Define the frontend directory.
    FRONTEND_DIRECTORY: pathlib.Path

    # Set the frontend directory.
    def _set_frontend_directory(self: "Frontend") -> None:
        # Convert the root to a path.
        root: pathlib.Path = pathlib.Path(self.root)

        # Set the directory.
        self.FRONTEND_DIRECTORY = pathlib.Path(root / "frontend" / "app")

    # Get build tool.
    def _get_tool(self: "Frontend", tool: str) -> str:
        # Get the tool.
        binary: str | None = shutil.which(tool)

        # Check if the tool exists.
        if binary is None:
            # Get class name.
            name: str = self.__class__.__name__

            # Raise an error.
            raise BoterviewBuildError(f"Tool \"{tool}\" required by \"{name}\" build hook not found in \"PATH\".")

        # Return the path.
        return binary

    # Remove a directory silently.
    def _remove_directory(self: "Frontend", directory: pathlib.Path) -> None:
        # Remove the directory.
        shutil.rmtree(directory, ignore_errors = True)

    # Define a method to run a subprocess.
    def _run_subprocess(self: "Frontend", command: List[str], directory: pathlib.Path) -> None:
        # Print the command.
        self.app.display_waiting(f"-- running command: \"{" ".join(command)}\" in directory: \"{directory}\"")

        # Run the command.
        subprocess.run(command, cwd = directory, check = True)

    # The constructor.
    def __init__(self: "Frontend", *args, **kwargs) -> None:
        # Call the parent constructor.
        super().__init__(*args, **kwargs)

        # Set the frontend directory.
        self._set_frontend_directory()

    # The method called when the hook is executed with the clean flag.
    def clean(self: "Frontend", versions: List[str]) -> None:
        # Remove the UI dependencies.
        self._remove_directory(self.FRONTEND_DIRECTORY / "node_modules")

        # Remove any previous UI build.
        self._remove_directory(self.FRONTEND_DIRECTORY / "dist")

        # Print a message.
        self.app.display_success("Successfully cleaned frontend artifacts before the build process.")

    # The method called before the build process.
    def initialize(self: "Frontend", version: str, build_data: Dict[str, Any]) -> None:
        # Attempt to build the frontend.
        try:
            # Get the `pnpm` binary.
            pnpm: str = self._get_tool("pnpm")

            # Install the UI dependencies.
            self._run_subprocess([pnpm, "install", "--frozen-lockfile"], self.FRONTEND_DIRECTORY)

            # Build the UI.
            self._run_subprocess([pnpm, "run", "build"], self.FRONTEND_DIRECTORY)

        # In case of user interrupt.
        except KeyboardInterrupt:
            # Print a message.
            self.app.abort("\nInterrupt: Build process interrupted by user.")

            # Exit the process.
            sys.exit(1)

        # In case of build error.
        except BoterviewBuildError as error:
            # Print the error.
            self.app.display_error(f"Build error: {error}")

            # Exit the process.
            sys.exit(1)

        # In case of generic error.
        except Exception as error:
            # Print the error.
            self.app.display_error(f"Unexpected error: {error}")

            # Exit the process.
            sys.exit(1)

        # Print a message.
        self.app.display_success("Frontend build completed successfully.")

    # The method called after the build process.
    def finalize(self, version: str, build_data: Dict[str, Any], artifact_path: str) -> None:
        # Remove the UI dependencies.
        self._remove_directory(self.FRONTEND_DIRECTORY / "node_modules")

        # Remove the UI build artifacts.
        self._remove_directory(self.FRONTEND_DIRECTORY / "dist")

        # Print a message.
        self.app.display_success("Successfully cleaned frontend artifacts after the build process.")
