import httpx

from .fmtypes import SearchType


def search(query: str, search_type: str = SearchType.all):
    params = {
        "q": query,
        "type": search_type,
    }
    r = httpx.get("https://kerve.last.fm/kerve/search", params=params)
    return r.json()

