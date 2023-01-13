#!/usr/bin/env python3
"""
sum_mixed_list which takes a list mxd_lst of integers
and floats and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    takes a list mxd_lst of integers and floats as argument
     and returns their sum as a float
    :param mxd_lst:
    :return: sum of mxd_lst elements as float
    """
    return sum(mxd_lst)
