#!/usr/bin/env python3
"""
Calculate the start and end indices for a given page and page_size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index and an end index
    """
    end: int = page * page_size
    start: int = end - page_size

    return (start, end)
