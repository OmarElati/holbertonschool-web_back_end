#!/usr/bin/env python3
"""
Password hashing
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Encrypting passwords """
    p = password.encode()
    return bcrypt.hashpw(p, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Use bcrypt to validate that provided password matches hashed password.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
