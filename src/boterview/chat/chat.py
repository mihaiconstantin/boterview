# Imports.
from typing import Dict
import chainlit

# Import helpers.
import boterview.helpers.authentication as authentication


# On user authentication.
@chainlit.header_auth_callback # type: ignore
def header_auth_callback(headers: Dict) -> chainlit.User | None:
    # If the cookie header is not present.
    if not (cookie := headers.get("cookie")):
        # Signal unauthenticated.
        return None

    # Parse the cookie header.
    cookies: Dict[str, str] = authentication.parse_cookie(cookie)

    # Attempt to decode the JWT.
    try:
        # Decode the JWT.
        code: str = authentication.decode_jwt(cookies["code"])

    # Catch any exceptions.
    except Exception:
        # Signal unauthenticated.
        return None

    # Return the user to signal authentication.
    return chainlit.User(identifier = code)
