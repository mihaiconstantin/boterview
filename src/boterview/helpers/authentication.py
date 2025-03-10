# Imports.
from typing import Callable, Dict
import jwt
from datetime import datetime, timedelta, timezone


# Parse the cookie header as a dictionary.
def parse_cookie(cookie: str) -> Dict[str, str]:
    # Create a dictionary from the header cookie.
    cookies: Dict[str, str] = dict(part.split("=") for part in cookie.split(";"))

    # Return the cookies.
    return cookies


# Create a JWT from the participation code.
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
