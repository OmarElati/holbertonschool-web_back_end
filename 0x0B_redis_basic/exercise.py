#!/usr/bin/env python3
"""
Cache Module

This module provides a Cache class that interacts with Redis for caching data.

Classes:
    Cache: A class for caching data in Redis.
"""
import redis
import uuid
from typing import Union


class Cache:
    """A class for caching data in Redis."""
    def __init__(self):
        """
        Initialize a Cache instance.
        Creates a Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return the generated key.

        Args:
            data: Data to be stored. Can be of type str, bytes, int, or float.

        Returns:
            str: The key under which the data is stored in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
