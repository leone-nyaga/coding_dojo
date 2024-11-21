import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size two containing a start index and an end index"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a list of rows for the specified page."""
        assert isinstance(page, int) and page > 0, "Page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be an integer greater than 0"

        # Get the dataset
        dataset = self.dataset()

        # Use index_range to get the start and end indexes for the page
        start_index, end_index = index_range(page, page_size)

        # Check if the requested page is out of range
        if start_index >= len(dataset):
            return []  # Return an empty list if out of range

        # Return the appropriate slice of the dataset
        return dataset[start_index:end_index]
