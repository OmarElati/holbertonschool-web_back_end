#!/usr/bin/env python3
"""
Import async_generator from the previous
task and then write a coroutine called
async_comprehension that takes no arguments.
"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 random numbers using an async
    comprehensing over async_generator
    """
    return [random_number async for random_number in async_generator()]
