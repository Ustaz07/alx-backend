#!/usr/bin/env python3
""" LIFO caching system """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching
        and implements a LIFO caching system.
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.last_key = None  # Track the last inserted key

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]

            self.cache_data[key] = item
            self.last_key = key  # Update the last inserted key

            # Check if cache exceeds MAX_ITEMS and discard the last inserted item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
