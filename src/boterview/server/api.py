# Imports.
from typing import Dict, List
from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from boterview.services.ui.ui import UI

# Import helpers.
import boterview.helpers.authentication as authentication

# Import the application context.
import boterview.context.app as app


# Create a new API router.
router = APIRouter(prefix = "/api")


# Define a route to get an UI element content by key.
@router.get("/ui/{key}")
async def ui(key: str, request: Request) -> JSONResponse:
    # Define the list of elements not requiring authentication.
    no_authentication: List[str] = ["welcome", "footer"]

    # If the element is not welcomed.
    if key not in no_authentication and not authentication.is_authenticated(request):
        # Return an unauthorized response.
        return JSONResponse(
            content = {"status": "error", "message": "Authentication required."},
            status_code = status.HTTP_401_UNAUTHORIZED
        )

    # Get the current user interface from the context.
    ui: UI = app.get_ui()

    # If the element is not found.
    if key not in ui.elements:
        # Return a not found response.
        return JSONResponse(
            content = {"status": "error", "message": "UI element not found."},
            status_code = status.HTTP_404_NOT_FOUND
        )

    # Overwise, prepare the response data.
    data: Dict[str, str | List[str] | Dict[str, str] | None] = {
        "heading": ui.elements[key].heading,
        "content": ui.elements[key].content,
        "metadata": ui.elements[key].metadata
    }

    # Return the response.
    return JSONResponse(
        content = {"status": "success", "data": data},
        status_code = status.HTTP_200_OK
    )
