#!/usr/bin/env python3
"""
auth.py

contains authentication functions and classes.
"""

from flask import request
from typing import TypeVar, List


User = TypeVar('User')


class Auth:
    """Auth class containing authentication functions."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for a path.

        Args:
            path: The path to check.
            excluded_paths: List of paths that do not require auth.

        Returns:
            True if path requires authentication, False otherwise.
        """
        check = path
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            check += "/"
        if check in excluded_paths or path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Return the authorization header from a request.

        Args:
            request: The request to get the header from.

        Returns:
            The authorization header string or None if missing.
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> User:
        """Return the current user from the request.

        Args:
            request: The request to extract the user from.

        Returns:
            The current user object or None if not found.
        """
        return None
