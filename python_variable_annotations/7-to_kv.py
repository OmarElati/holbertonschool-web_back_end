#!/usr/bin/env python3
"""
Returns a tuple with the string 'k' and the square of 'v' as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    param k: The input string.
    param v: The input integer or float.
    return: A tuple containing 'k' and the square of 'v' as a float.
    """
    return (k, float(v ** 2))
