#!/usr/bin/env python3
"""
auth.py

contains authentication functions and classes.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class for handling authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if the given path requires authentication.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != "/":
            path += "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Return the authorization header for the request.
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """Return the currently authenticated user.
        """
        return None
