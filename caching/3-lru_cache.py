#!/usr/bin/python3
"""
class LRUCache that inherits from
BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class """

    def __init__(self):
        """ Initialize LRUCache """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.keys.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        self.keys.remove(key)
        self.keys.append(key)

        return self.cache_data[key]
