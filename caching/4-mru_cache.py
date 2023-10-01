#!/usr/bin/python3
"""
class MRUCache that inherits from
BaseCaching and is a caching system.
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class """

    def __init__(self):
        """ Initialize MRUCache """
        super().__init__()
        self.lst = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.lst.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = self.lst.pop(-2)
            print('DISCARD:', last)
            del self.cache_data[last]

    def get(self, key):
        """ Retrieve an item from the cache """
        if key in self.cache_data:
            self.lst.append(key)
        if key in self.cache_data:
            return self.cache_data[key]
