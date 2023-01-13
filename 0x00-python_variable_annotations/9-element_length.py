#!/usr/bin/env python3
"""typed the function"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    takes iterable of sequence and returns list of tuple of
    sequence as fist element and int as second element
    :param lst:
    :return:list of tuple of sequence as fist element and int as second element
    """
    return [(i, len(i)) for i in lst]
