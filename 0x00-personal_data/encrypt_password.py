#!/usr/bin/env python3
"""
Task 5 & 6: Encrypting passwords
Implement a hash_password function that returns a salted, hashed password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypts a password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    checks if a given password matches a hashed password using the bcrypt
    algorithm.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
