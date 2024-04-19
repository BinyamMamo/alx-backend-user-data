#!/usr/bin/env python3
"""
basic_auth.py

"""
from api.v1.auth.auth import Auth
from flask import request
from models.user import User
from typing import List, TypeVar, Tuple
import base64
import binascii


class BasicAuth(Auth):
    """Auth class for handling authentication."""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts base64 encoded auth header"""
        if (
            authorization_header is None
            or not isinstance(authorization_header, str)
            or not authorization_header.startswith("Basic")
        ):
            return None
        return authorization_header[len("Basic") + 1:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decodes a base64 encoded string"""
        if type(base64_authorization_header) == str:
            try:
                res = base64.b64decode(
                    base64_authorization_header,
                    validate=True,
                )
                return res.decode("utf-8")
            except (binascii.Error, UnicodeDecodeError):
                return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        Extracts the user email and password from
        the Base64 decoded authorization header
        """
        if (not isinstance(decoded_base64_authorization_header, str) or
                ":" not in decoded_base64_authorization_header):
            return (None, None)

        return tuple(decoded_base64_authorization_header.split(":", 1))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Checks if user email and password
        match a user object in the database
        """
        if (isinstance(user_email, str) and
                isinstance(user_pwd, str)):
            result = User.search({"email": user_email})

            if (result and len(result) > 0 and
                    result[0].is_valid_password(user_pwd)):
                return result[0]

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the authenticated user from the request
        """
        header = self.authorization_header(request)
        if header is None:
            return None
        header64 = self.extract_base64_authorization_header(header)
        if header64 is None:
            return None
        decoded_header = self.decode_base64_authorization_header(header64)
        if decoded_header is None:
            return None
        credentials = self.extract_user_credentials(decoded_header)
        if credentials is None:
            return None
        user = self.user_object_from_credentials(credentials)

        return user

