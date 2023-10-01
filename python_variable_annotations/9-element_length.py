#!/usr/bin/env python3
"""
Computes the length of each element in
the input list and returns a list of tuples
where each tuple contains an element from
the input list and its length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) \
        -> List[Tuple[Sequence, int]]:
    """
    param lst: The input iterable of sequences.
    return: A list of tuples where each tuple contains an element and its length.
    """
    return [(i, len(i)) for i in lst]
