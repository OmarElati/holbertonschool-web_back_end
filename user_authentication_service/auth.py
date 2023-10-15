#!/usr/bin/env python3
"""
Hash password, Register user, Credentials validation, Generate UUIDs,
Find user by session ID, Destroy session, Generate reset password token,
Update password
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt with a random salt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        existing_user = self._db.find_user_by(email=email)
        if existing_user:
            raise ValueError(f"User {email} already exists")

        hashed_password = _hash_password(password)

        new_user = self._db.add_user(email, hashed_password)
        return new_user
