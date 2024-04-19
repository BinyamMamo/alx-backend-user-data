"""
Module containing authentication classes and functions.
"""
from flask import request
from typing import List


class Auth:
    """Auth class for handling authentication."""
    
    def __init__(self) -> None:
        """Initialize the Auth instance."""
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if the given path requires authentication.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Return the authorization header for the request.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the currently authenticated user.
        """
        return None
