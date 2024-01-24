#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union


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


if __name__ == "__main__":
    cache = Cache()

    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = redis.Redis()
    print(local_redis.get(key))
