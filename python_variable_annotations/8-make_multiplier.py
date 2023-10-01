#!/usr/bin/env python3
"""
Returns a function that multiplies a float by the given multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    param multiplier: The multiplier to be used
                      in the returned function.
    return: A function that takes a float and returns
            the result of multiplying it by the multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
