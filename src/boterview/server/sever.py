# Imports.
from typing import List
import os
import pathlib
from fastapi import FastAPI, status
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Database models.
from boterview.models.database.conversation import Conversation
from boterview.models.database.participant import Participant

# Import the context.
import boterview.context.app as app
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

    # If the server is started in headless mode.
    if server.state.headless:
        # Define the index route.
        @server.get("/")
        def headless_index():
            return JSONResponse(
                content = {
                    "status": "success",
                    "message": "The server is running in headless mode."
                },
                status_code = status.HTTP_200_OK
            )

        # Return early.
        return

    # Otherwise, mount the frontend.

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
    def frontend_index(path: str):
        # Get the requested file.
        requested_file = FRONTEND_APP_BUILD / path

        # If the requested file is a file.
        if requested_file.is_file():
            # Serve the requested file.
            return FileResponse(str(requested_file))

        # Otherwise, serve the index file.
        return FileResponse(FRONTEND_APP_BUILD / "index.html")


# Mount the chat application.
def mount_chat(server: FastAPI):
    # Get the secret key from the configuration.
    SECRET_KEY = app.get_configuration().data["app"]["secret_key"]

    # Get the package root directory.
    PACKAGE_SOURCE: pathlib.Path = path.get_package_source()

    # Get the package root directory.
    PACKAGE_ROOT: pathlib.Path = path.get_package_root()

    # Set the chat application path.
    os.environ["CHAINLIT_APP_ROOT"] = str(PACKAGE_ROOT / "frontend" / "chat")

    # Set the `chainlit` authentication variables.
    os.environ["CHAINLIT_AUTH_SECRET"] = SECRET_KEY

    # Local imports.
    from chainlit.utils import mount_chainlit

    # Mount the `chainlit` instance.
    mount_chainlit(
        app = server,
        target = str(PACKAGE_SOURCE / "chat" / "chat.py"),
        path = "/chat/"
    )


# Add `CORS` middleware.
def add_cors_middleware(server: FastAPI, origins: List[str]):
    # Add CORS middleware to the server.
    server.add_middleware(
        CORSMiddleware,
        allow_origins = origins,
        allow_credentials = True,
        allow_methods = ["*"],
        allow_headers = ["*"],
        expose_headers = ["Content-Disposition"]
    )


# Create a server instance.
def create_server(database: str, headless: bool) -> FastAPI:
    # Create a lifespan event handler.
    lifespan = create_lifespan(database)

    # Create a `FastAPI` instance.
    server: FastAPI = FastAPI(
        lifespan = lifespan,
        title = "Boterview",

        # Disable API documentation.
        docs_url = None,
        redoc_url = None,
        openapi_url = None
    )

    # Store the headless flag on the state.
    server.state.headless = headless

    # Mount the chat application.
    mount_chat(server)

    # Mount the frontend application.
    mount_frontend(server)

    # Return the server instance.
    return server
