#!/usr/bin/env python3
"""
basic_auth.py

"""
from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar


class BasicAuth(Auth):
    """Auth class for handling authentication."""
