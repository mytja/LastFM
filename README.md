# LastFM
Get charts, top artists and top songs WITHOUT LastFM API

# Usage

## Get stats (charts)
We provide many filters and options to customize. Geo filter is only one, that doesn't have a specific enum (class).
```py
from lastfm import *

print(get_charts(SearchType.artists))
print(get_charts(SearchType.tracks,
                 geo_filter="si",
                 music_type_filter=MusicTypeFilter.electronic,
                 limit=1,
                 year_filter=YearFilter.t2010s))
```

## Search
We also provide searching.
```py
from lastfm import *

print(search("Glass Animals", search_type=SearchType.all))
```
