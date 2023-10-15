#!/usr/bin/env python3
"""
Hash password, Register user, Credentials validation, Generate UUIDs,
Find user by session ID, Destroy session, Generate reset password token,
Update password
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt with a random salt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
