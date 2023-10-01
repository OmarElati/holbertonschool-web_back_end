#!/usr/bin/env python3
"""
Asynchronous coroutine that waits for
a random delay between 0 and max_delay seconds
(inclusive) and returns it as a float.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    param max_delay: The maximum delay in seconds (default is 10).
    return: The random delay as a float.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
