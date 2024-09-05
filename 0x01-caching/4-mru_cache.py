#!/usr/bin/env python3
""" MRU caching system """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching
        and implements an MRU caching system.
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()
        self.access_order = []  # List to track the order of key access

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        # If the key is already in the cache, remove it to update the order later
        if key in self.cache_data:
            self.access_order.remove(key)

        # Add the new item to cache and update access order
        self.cache_data[key] = item
        self.access_order.append(key)

        # Check if cache exceeds MAX_ITEMS and discard the most recently used item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.access_order.pop()  # The last element is the most recently used
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Update the access order since this key was recently accessed
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
