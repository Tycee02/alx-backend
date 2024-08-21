#!/usr/bin/python3
"""
LRU caching
"""

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Represents an object that allows storing and
    retrieving items from a dictionary with a LRU
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initialize the cache system."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache."""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Get an item by key from the cache."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
