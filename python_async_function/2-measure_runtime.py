#!/usr/bin/env python3
"""
Measures the total execution time for wait_n(n, max_delay) and returns total_time / n.
"""
from typing import List
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    param n: The number of times to call wait_n.
    param max_delay: The maximum delay in seconds for wait_random.
    return: The average execution time per call.
    """
    start_time = time.time()

    await asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time

    return total_time / n
