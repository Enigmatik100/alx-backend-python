#!/usr/bin/env python3
"""2. Measure the runtime"""
from asyncio import run
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time
    :param n:
    :param max_delay:
    :return: execution time
    """
    start_time = time()
    run(wait_n(n, max_delay))
    end_time = time()
    return (end_time - start_time) / n
