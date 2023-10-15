#!/usr/bin/env python3
"""
Hash password, Register user, Credentials validation, Generate UUIDs,
Find user by session ID, Destroy session, Generate reset password token,
Update password
"""
import bcrypt
from bcrypt import hashpw, gensalt, checkpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
import uuid

def _hash_password(password: str) -> str:
    """ Takes in string arg, converts to unicode
    Returns salted, hashed pswd as bytestring
    """
    return hashpw(password.encode('utf-8'), gensalt())


def _generate_uuid() -> str:
    """ Generates UUID
    Returns string representation of new UUID
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers and returns a new user if email isn't listed """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """ Checks if user pswd is valid, locating by email """
        try:
            found_user = self._db.find_user_by(email=email)
            return checkpw(
                password.encode('utf-8'),
                found_user.hashed_password
                )
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ Creates session ID using UUID, finds user by email """
        try:
            found_user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = str(uuid.uuid4())
        self._db.update_user(found_user.id, session_id=session_id)
        return session_id
