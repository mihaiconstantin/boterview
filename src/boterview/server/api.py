# Imports.
from typing import Dict, List
from datetime import datetime, timezone
from fastapi import APIRouter, Request, Response, status
from fastapi.responses import JSONResponse
from boterview.models.api.code import CodePayload
from boterview.models.api.participant import ParticipantPayload
from boterview.models.api.secret import SecretPayload
from boterview.services.boterview.boterview import Boterview
from boterview.services.configuration.configuration import Configuration
from boterview.services.ui.ui import UI

# Import database models.
from boterview.models.database.participant import Participant as ParticipantModel

# Import helpers.
import boterview.helpers.authentication as authentication
import boterview.helpers.storage as storage

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


# Define a participant code verification API endpoint.
@router.post("/verify")
async def verify(payload: CodePayload) -> JSONResponse:
    # Strip the code of any whitespace.
    code = payload.code.strip()

    # Get the current `boterview` instance.
    boterview: Boterview = app.get_boterview()

    # Check the code against the allowed list of codes.
    code_is_valid = boterview.validate_code(code)

    # If the code is not valid.
    if not code_is_valid:
        return JSONResponse(
            content = {"status": "error", "message": "Invalid participation code."},
            status_code = status.HTTP_401_UNAUTHORIZED
        )

    # Create a new participant model.
    ParticipantModel.create(code = code)

    # Prepare the response.
    response: Response = JSONResponse(
        content = {"status": "success", "message": "Valid participation code."},
        status_code = status.HTTP_200_OK
    )

    # Create a JWT token from the code.
    token: str = authentication.create_jwt(code)

    # Attach token as a cookie to the response.
    response.set_cookie(
        key = "code",
        value = token,
        httponly = True
    )

    # Return the response.
    return response


# Define a participant consent endpoint.
@router.post("/consent")
async def consent(payload: ParticipantPayload, request: Request) -> JSONResponse:
    # Get the code from the cookie by decoding the JWT.
    code: str | None  = authentication.get_code(request)

    # If the code is missing, return an unauthorized response.
    if not code:
        # Return the response.
        return JSONResponse(
            content = {"status": "error", "message": "Authentication required."},
            status_code = status.HTTP_401_UNAUTHORIZED
        )

    # If the user hasn't consented.
    if not payload.consented:
        # Return the response.
        return JSONResponse(
            content = {"status": "error", "message": "Consent not given."},
            status_code = status.HTTP_401_UNAUTHORIZED
        )

    # Get the participant by the code.
    participant: ParticipantModel = storage.get_participant(code)

    # Update the consent status.
    participant.consent = True # type: ignore

    # Save the participant.
    participant.save()

    # Prepare the response.
    response: Response = JSONResponse(
        content = {"status": "success", "message": "Consent processed."},
        status_code = status.HTTP_200_OK
    )

    # Attach token as a cookie to the response.
    response.set_cookie(
        key = "consent",
        value = datetime.now(timezone.utc).isoformat(),
        httponly = True
    )

    # Return the response.
    return response


# Define an action endpoint.
@router.post("/action")
async def action(request: Request) -> JSONResponse:
    # If the user is not authenticated.
    if not authentication.is_authenticated(request):
        # Return the response.
        return JSONResponse(
            content = {"status": "error", "message": "Authentication required."},
            status_code = status.HTTP_401_UNAUTHORIZED
        )

    # If the user is authenticated, get the request body.
    body: Dict = await request.json()

    # Get the action from the request body.
    action: str | None = body.get("action")

    # If the action is not present.
    if action is None:
        # Return the response.
        return JSONResponse(
            content = {"status": "error", "message": "Action not specified."},
            status_code = status.HTTP_400_BAD_REQUEST
        )

    # If the action is `stop`.
    if action == "stop":
        # Return a redirect response to the client `/stop` endpoint.
        return JSONResponse(
            content = {"status": "success", "url": "/stop"},
            status_code = status.HTTP_200_OK
        )

    # For any unknown action.
    return JSONResponse(
        content = {"status": "error", "message": "Invalid action."},
        status_code = status.HTTP_400_BAD_REQUEST
    )


# Define a logout endpoint.
@router.post("/logout")
async def logout(request: Request) -> JSONResponse:
    # Get the code from the cookie by decoding the JWT.
    code: str | None  = authentication.get_code(request)

    # If the code is missing, return an unauthorized response.
    if not code:
        # Return the response.
        return JSONResponse(
            content = {"status": "error", "message": "Authentication required."},
            status_code = status.HTTP_401_UNAUTHORIZED
        )

    # Get the participant by the code.
    participant: ParticipantModel = storage.get_participant(code)

    # Update the participant record in the database.
    participant.end_time = datetime.now(timezone.utc) # type: ignore

    # Save the participant record.
    participant.save()

    # Prepare the redirect response.
    response = JSONResponse(
        content = {"status": "success", "message": "Logout successful."},
        status_code = status.HTTP_200_OK
    )

    # Delete the cookies.
    response.delete_cookie("code")
    response.delete_cookie("consent")
    response.delete_cookie("access_token")

    # Return the response.
    return response


# Define a markdown download data endpoint.
@router.post("/download")
async def download(payload: SecretPayload) -> Response:
    # Get the current configuration instance.
    configuration: Configuration = app.get_configuration()

    # Get the secret key from the configuration.
    secret: str = configuration.data["app"]["secret_key"]

    # Validate the secret key.
    if payload.secret != secret:
        # Return an unauthorized response.
        return JSONResponse(
            content = {"status": "error", "message": "Unauthorized access."},
            status_code = status.HTTP_401_UNAUTHORIZED
        )

    # Get the `boterview` instance from the context.
    boterview: Boterview = app.get_boterview()

    # Parse the database and get the content as a string.
    content: str = storage.parse_database(boterview)

    # Format the study name.
    study_name: str = (boterview.study.name or "Interview Study").lower().replace(" ", "-")

    # Format the download timestamp.
    timestamp: str = datetime.now(timezone.utc).strftime("%Y-%m-%d-%H-%M-%S")

    # Define the headers.
    headers: Dict[str, str] = {
        f"Content-Disposition": f"attachment; filename=output-{study_name}-{timestamp}.md"
    }

    # Return the response.
    return Response(
        content = content,
        media_type = "text/markdown",
        headers = headers
    )
