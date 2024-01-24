#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """
    A simple cache implementation using Redis.
    """

    def __init__(self):
        """
        Initialize the Cache instance with a Redis client and flush the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in the cache and return the generated key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored in the cache.

        Returns:
            str: The generated key used to store the data in the cache.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, None]:
        """
        Retrieve data from the cache using the given key and optionally apply a conversion function.

        Args:
            key (str): The key used to retrieve data from the cache.
            fn (Callable, optional): A callable function to convert the retrieved data. Defaults to None.

        Returns:
            Union[str, bytes, int, None]: The retrieved data, optionally converted by the provided function.
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve a string from the cache using the given key.

        Args:
            key (str): The key used to retrieve the string from the cache.

        Returns:
            Union[str, None]: The retrieved string, or None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve an integer from the cache using the given key.

        Args:
            key (str): The key used to retrieve the integer from the cache.

        Returns:
            Union[int, None]: The retrieved integer, or None if the key does not exist.
        """
        return self.get(key, fn=int)


if __name__ == "__main__":
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value
