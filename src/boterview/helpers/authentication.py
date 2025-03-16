# Imports.
from typing import Callable, Dict
import jwt
from fastapi import Request
from datetime import datetime, timedelta, timezone
from boterview.services.configuration.configuration import Configuration

# Import the application context.
import boterview.context.app as app


# Parse the cookie header as a dictionary.
def parse_cookie(cookie: str) -> Dict[str, str]:
    # Create a dictionary from the header cookie.
    cookies: Dict[str, str] = dict(part.strip().split("=") for part in cookie.split(";"))

    # Return the cookies.
    return cookies


# Decorator to inject the application secret for the JWT functions.
def with_application_secret(function: Callable[..., str]) -> Callable[..., str]:
    # Define the wrapper function.
    def wrapper(*args, **kwargs) -> str:
        # Get the configuration.
        configuration: Configuration = app.get_configuration()

        # Get the secret key.
        secret: str = configuration.data["app"]["secret_key"]

        # Call the function with the secret key.
        return function(*args, **kwargs, secret = secret)

    # Return the wrapper.
    return wrapper


# Create a JWT from the participation code.
@with_application_secret
def create_jwt(code: str, secret: str) -> str:
    # If the secret is not provided.
    if not secret:
        # Raise.
        raise ValueError(f"Invalid secret \"{ secret }\" provided for JWT creation.")

    # Create the payload.
    payload = {
        # The participation code.
        "code": code,

        # Add the expiration time (i.e., three days from now).
        "exp": datetime.now(timezone.utc) + timedelta(seconds = 259200),

        # Add the issued at time.r
        "iat": datetime.now(timezone.utc)
    }

    # Create the JWT.
    encoded_jwt: str = jwt.encode(payload, secret, algorithm = "HS256")

    # Return the encoded JWT.
    return encoded_jwt


# Decode the JWT from the participation code.
@with_application_secret
def decode_jwt(token: str, secret) -> str:
    # If the secret is not provided.
    if not secret:
        # Raise.
        raise ValueError(f"Invalid secret \"{ secret }\" provided for JWT decoding.")

    # Decode the JWT.
    decoded_jwt: Dict[str, str] = jwt.decode(
        jwt = token,
        key = secret,
        algorithms = ["HS256"],
        options = {"verify_signature": True}
    )

    # Return the code.
    return decoded_jwt["code"]


# Define a function to check if the user is authenticated.
def is_authenticated(request: Request) -> bool:
    # Retrieve the code cookie.
    code_cookie: str | None = request.cookies.get("code")

    # If the code cookie is not present.
    if not code_cookie:
        return False

    # Attempt to decode the code cookie.
    try:
        # Decode the code cookie.
        decode_jwt(code_cookie)

    # Catch any exceptions.
    except Exception:
        return False

    # Return authenticated.
    return True


# Get the code from the request.
def get_code(request: Request) -> str | None:
    # Retrieve the code cookie.
    code_cookie: str | None = request.cookies.get("code")

    # If the code cookie is not present.
    if not code_cookie:
        # Return.
        return None

    # Attempt to decode the code cookie.
    try:
        # Decode the code cookie
        code: str = decode_jwt(code_cookie)

        # Return the code.
        return code

    # Catch any exceptions.
    except Exception:
        # Return.
        return None
