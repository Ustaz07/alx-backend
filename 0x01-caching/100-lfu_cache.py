#!/usr/bin/env python3
""" LFU Caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines a caching system with LFU eviction """

    def __init__(self):
        """ Initialize class """
        super().__init__()
        self.usage_count = {}  # To track the frequency of each key
        self.recently_used = []  # To track the order of access (LRU)

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        # Update item and usage if key already exists
        if key in self.cache_data:
            self.cache_data[key] = item
            self.usage_count[key] += 1
            self._update_access_order(key)
            return

        # Evict the least frequently used item if over capacity
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self._evict_item()

        # Add the new item
        self.cache_data[key] = item
        self.usage_count[key] = 1
        self.recently_used.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Update usage statistics
        self.usage_count[key] += 1
        self._update_access_order(key)
        return self.cache_data[key]

    def _evict_item(self):
        """ Evict the least frequently used item from the cache """
        # Find the item(s) with the lowest usage count
        min_freq = min(self.usage_count.values())
        candidates = [k for k in self.recently_used if self.usage_count[k] == min_freq]

        # Use LRU strategy to decide among the least frequently used
        if candidates:
            evict_key = candidates[0]
            self.recently_used.remove(evict_key)
            del self.cache_data[evict_key]
            del self.usage_count[evict_key]
            print(f"DISCARD: {evict_key}")

    def _update_access_order(self, key):
        """ Update the order of access for LRU management """
        if key in self.recently_used:
            self.recently_used.remove(key)
        self.recently_used.append(key)
