#!/usr/bin/env python3
"""
Implement a get_hyper method that
takes the same arguments (and defaults)
as get_page and returns a dictionary
containing the following key-value pairs
"""
from typing import Tuple, List, Dict, Union
import csv
import math


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        return a tuple of size two containing a start index and an end index
        """
        end: int = page * page_size
        start: int = 0
        for _ in range(page - 1):
            start += page_size
        return (start, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get page
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        dataset = self.dataset()
        start, end = self.index_range(page, page_size)
        if end > len(dataset):
            return []
        return [list(dataset[row]) for row in range(start, end)]

    def get_hyper(self, page: int = 1, page_size: int = 10) ->\
            Dict[str, Union[List[List], None, int]]:
        """
        get page and return dict
        """
        data: List = self.get_page(page, page_size)
        size_dataset: int = len(self.dataset())
        totalPage = math.ceil(size_dataset / page_size)
        if page - 1 == 0:
            prev_page = None
        else:
            prev_page = page - 1

        if page + 1 > size_dataset or data == []:
            next_page = None
        else:
            next_page = page + 1

        if data is not []:
            pageSize = page_size

        hateoas: Dict = {'page_size': pageSize,
                         'page': page,
                         'data': data,
                         'next_page': next_page,
                         'prev_page': prev_page,
                         'total_pages': totalPage}
        return hateoas
