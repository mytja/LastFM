import urllib.parse

import httpx


class ChartType:
    artists = "artist"
    tracks = "track"


class YearFilter:
    t1920s = "tag:1920s"
    t1930s = "tag:1930s"
    t1940s = "tag:1940s"
    t1950s = "tag:1950s"
    t1960s = "tag:1960s"
    t1970s = "tag:1970s"
    t1980s = "tag:1980s"
    t1990s = "tag:1990s"
    t2000s = "tag:2000s"
    t2010s = "tag:2010s"


class MusicTypeFilter:
    rock = "tag:Rock"
    electronic = "tag:Electronic"
    indie = "tag:Indie"
    pop = "tag:Pop"
    metal = "tag:Metal"
    hip_hop = "tag:Hip Hop"
    punk = "tag:Punk"
    dance = "tag:Dance"
    chillout = "tag:Chillout"
    experimental = "tag:Experimental"


def get_charts(
        request_type: str,
        limit: int = 30,
        track_limit_per_artist: int = 1,
        year_filter: str = None,
        music_type_filter: str = None,
        geo_filter: str = None
):
    url = "https://kerve.last.fm/kerve/charts"
    params = {}

    k = urllib.parse.urlencode({"f": music_type_filter}) if music_type_filter else ""
    k += ("&" + urllib.parse.urlencode({"f": year_filter})) if year_filter else ""
    k += ("&" + urllib.parse.urlencode({"f": f"tag:{geo_filter.lower()}"})) if geo_filter else ""
    if request_type == ChartType.artists:
        params.update({
            "type": request_type,
            "tracks": track_limit_per_artist,
            "nr": limit,
            "format": "json",
        })
    elif request_type == ChartType.tracks:
        params.update({
            "type": request_type,
            "nr": limit,
            "format": "json"
        })

    if geo_filter:
        params.update({
            "geo": 300,
            "users": 0,
            "tags": 0
        })

    url += "?" + k
    r = httpx.get(url, params=params)
    if r.status_code != 200:
        raise Exception(f"Failed to retrieve chart - Status code {r.status_code}, Response {r.text}")
    response = r.json()

    return response
