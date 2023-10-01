#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
import random
import asyncio
from typing import List, Union
import heapq


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay seconds
    (inclusive) and returns it as a float.

    param max_delay: The maximum delay in seconds (default is 10).
    return: The random delay as a float.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay
    and returns the list of all the delays (float values) in ascending order.

    param n: The number of times to call wait_random.
    param max_delay: The maximum delay in seconds for wait_random.
    return: The list of delays in ascending order.
    """
    delays = []

    async def _wait_random_with_index(i: int):
        nonlocal delays
        delay = await wait_random(max_delay)
        heapq.heappush(delays, (delay, i))

    await asyncio.gather(*[_wait_random_with_index(i) for i in range(n)])

    sorted_delays = [delay for delay, _ in sorted(delays)]
    return sorted_delays
