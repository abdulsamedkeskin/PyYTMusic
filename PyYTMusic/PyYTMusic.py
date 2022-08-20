from .search import Search
from typing import List, Dict
from .lyrics import Lyrics


class PyYTMusic():
    def __init__(self):
        pass

    def search(self, query: str, filter: List = None, limit: int = None) -> List[Dict]:
        search = Search()
        return search.search(query, filter, limit)

    def lyrics(self, name: str, browse_id: str) -> str:
        lyrics = Lyrics()
        return lyrics.lyrics(name, browse_id)
