#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing pagination data.

        Args:
            index (int): The starting index of the page.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary with pagination details including data, index,
                  next_index, and page_size.
        """
        indexed_data = self.indexed_dataset()

        # Ensure the index is within valid range
        assert isinstance(index, int) and 0 <= index < len(indexed_data), \
            "index must be a positive integer within the dataset range"

        data = []
        current_index = index

        # Collect data items until we gather page_size elements
        while len(data) < page_size and current_index < len(indexed_data):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        next_index = current_index  # Set the next index for pagination

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
