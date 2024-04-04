#!/usr/bin/env python3
"""
Cache Module

This module provides a Cache class that interacts with Redis for caching data.

Classes:
    Cache: A class for caching data in Redis.
"""
import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis based on the given key.

        Args:
            key (str): The key associated with the data to be retrieved.
            fn (Callable, optional): A callable function used to convert the retrieved data.
                Defaults to None.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data.
        """
        if self._redis.exists(key):
            data = self._redis.get(key)
            if fn:
                return fn(data)
            return data
        return None

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve string data from Redis based on the given key.

        Args:
            key (str): The key associated with the string data to be retrieved.

        Returns:
            Union[str, None]: The retrieved string data.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve integer data from Redis based on the given key.

        Args:
            key (str): The key associated with the integer data to be retrieved.

        Returns:
            Union[int, None]: The retrieved integer data.
        """
        return self.get(key, fn=lambda d: int(d))
