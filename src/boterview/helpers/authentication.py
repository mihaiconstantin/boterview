# Imports.
from typing import Dict


# Parse the cookie header as a dictionary.
def parse_cookie(cookie: str) -> Dict[str, str]:
    # Create a dictionary from the header cookie.
    cookies: Dict[str, str] = dict(part.split("=") for part in cookie.split(";"))

    # Return the cookies.
    return cookies
