#!/usr/bin/env python3
"""
Pagination task
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.
    
    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.
    
    Returns:
        Tuple[int, int]: A tuple containing the start index and the end index.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset.
        
        Args:
            page (int): The current page number.
            page_size (int): The number of items per page.
        
        Returns:
            List[List]: A list of rows corresponding to the requested page.
        """
        # Assert that page and page_size are positive integers
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        # Get the dataset
        dataset = self.dataset()

        # Get the start and end indices for the page
        start, end = index_range(page, page_size)

        # Return the corresponding page of data or an empty list if out of range
        if start >= len(dataset):
            return []
        return dataset[start:end]
