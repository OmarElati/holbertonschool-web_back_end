#!/usr/bin/env python3
"""
Creates an asyncio.Task for the wait_random
coroutine with the specified max_delay.
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    param max_delay: The maximum delay in seconds for wait_random.
    return: An asyncio.Task representing the execution of wait_random.
    """
    delay_task = asyncio.create_task(wait_random(max_delay))
    return delay_task