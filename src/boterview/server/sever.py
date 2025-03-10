# Imports.
import pathlib
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# Database models.
from boterview.models.database.conversation import Conversation
from boterview.models.database.participant import Participant

# Import the context.
import boterview.context.persistence as persistence
import boterview.context.path as path


# Define a lifespan function factory.
def create_lifespan(database: str):
    # Local imports.
    from contextlib import asynccontextmanager

    # Define the lifespan event handler.
    @asynccontextmanager
    async def lifespan(server: FastAPI):
        # Startup.

        # Initialize the database connection.
        persistence.initialize_database(database)

        # Create the tables.
        persistence.database.create_tables([Participant, Conversation])

        # Yield control to the server.
        yield

        # Shutdown.

        # Close the database connection.
        persistence.database.close()

    # Return the lifespan event handler.
    return lifespan


# Mount the frontend application.
def mount_frontend(server: FastAPI):
    # Local imports.
    from boterview.server.api import router

    # Include the API router.
    server.include_router(router)

    # If the server is not headless.
    if not server.state.headless:
        # Get the package root directory.
        PACKAGE_ROOT: pathlib.Path = path.get_package_root()

        # Frontend directory.
        FRONTEND_APP_BUILD: pathlib.Path = PACKAGE_ROOT / "frontend" / "app" / "dist"

        # Check if the frontend build directory exists.
        if not FRONTEND_APP_BUILD.exists():
            # Raise an error.
            raise FileNotFoundError(f"Frontend build directory is missing. Please build the frontend.")

        # Mount the frontend build directory.
        server.mount(
            path = "/static",
            app = StaticFiles(directory = FRONTEND_APP_BUILD, html = True),
            name = "static"
        )

        # Catch all for the frontend.
        @server.get("/{path:path}", include_in_schema = False)
        def index(path: str):
            # Get the requested file.
            requested_file = FRONTEND_APP_BUILD / path

            # If the requested file is a file.
            if requested_file.is_file():
                # Serve the requested file.
                return FileResponse(str(requested_file))

            # Otherwise, serve the index file.
            return FileResponse(FRONTEND_APP_BUILD / "index.html")
