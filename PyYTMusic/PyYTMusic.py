from .search import Search
from typing import List, Dict


class PyYTMusic():
    def __init__(self):
        pass

    def search(self, query: str, filter: List = None) -> List[Dict]:
        search = Search()
        return search.search(query, filter)
