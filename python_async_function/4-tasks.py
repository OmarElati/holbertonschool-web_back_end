#!/usr/bin/env python3
"""
Creates a list of asyncio.Tasks to run
task_wait_random with the specified max_delay
and returns the results as a list of floats.
"""
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    param n: The number of times to call task_wait_random.
    param max_delay: The maximum delay in seconds for task_wait_random.
    return: A list of floats representing the results
            of task_wait_random calls.
    """
    tasks = []
    for i in range(n):
        tasks.append(await task_wait_random(max_delay))
    return sorted(tasks)
