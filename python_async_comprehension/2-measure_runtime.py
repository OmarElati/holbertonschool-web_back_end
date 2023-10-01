#!/usr/bin/env python3
"""
Import async_comprehension from the previous
file and write a measure_runtime coroutine
that will execute async_comprehension four
times in parallel using asyncio.gather.
"""


import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times
    and measure the total runtime.

    Returns the total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(async_comprehension())
    end_time = time.time()
    return end_time - start_time
