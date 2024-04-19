#!/usr/bin/env python3
"""
basic_auth.py

"""
from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar
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
