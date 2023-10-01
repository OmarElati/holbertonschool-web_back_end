#!/usr/bin/python3
"""
class FIFOCache that inherits from
BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class """

    def __init__(self):
        """ Initialize FIFOCache """
        super().__init__()

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")
                self.cache_data.pop(first_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
