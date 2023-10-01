#!/usr/bin/env python3
"""
Computes the sum of a list of integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    param mxd_lst: The list of integers and floats.
    return: The sum of the numbers as a floating-point number.
    """
    return sum(mxd_lst)
