#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float multiplier as argument and returns a function that multiplies
     a float by multiplier
    :param multiplier:
    :return: returns a function that multiplies a float by multiplier
    """
    return lambda a: a * multiplier
