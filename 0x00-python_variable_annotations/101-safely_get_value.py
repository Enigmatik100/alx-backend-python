#!/usr/bin/env python3
"""More involved type annotations"""
from typing import TypeVar, Mapping, Union, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    get safely value
    :param dct: dictionary
    :param key: the key of the dict
    :param default: value of None
    :return:
    """
    if key in dct:
        return dct[key]
    else:
        return default
