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

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = next(reversed(self.cache_data))
                print(f"DISCARD: {mru_key}")
                del self.cache_data[mru_key]
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the cache_data dictionary
        item = self.cache_data.pop(key)
        self.cache_data[key] = item

        return item
