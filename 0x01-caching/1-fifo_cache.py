#!/usr/bin/env python3
""" FIFO caching system """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching
        and implements a FIFO caching system.
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.order = []  # List to keep track of the order of insertion

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)

            # If cache exceeds MAX_ITEMS discard first inserted item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
