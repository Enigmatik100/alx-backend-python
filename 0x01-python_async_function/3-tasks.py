#!/usr/bin/env python3
"""3. Tasks"""
from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Write a function (do not create an async function,
    use the regular function syntax to do this)
    task_wait_randomthat takes an integer max_delay
    and returns a asyncio.Task.
    :param max_delay:
    :return: Task
    """
    task = create_task(wait_random(max_delay))
    return task
