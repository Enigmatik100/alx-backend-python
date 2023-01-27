#!/usr/bin/env python3
"""4. Tasks"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Task wait random
    :param n:
    :param max_delay:
    :return: the list of all the delays (float values).
    The list of the delays should be in ascending order
    without using sort() because of concurrency.
    """
    delays = []
    for res in asyncio.as_completed([task_wait_random(max_delay)
                                     for _ in range(n)]):
        completed_tasks = await res
        delays.append(completed_tasks)
    return delays