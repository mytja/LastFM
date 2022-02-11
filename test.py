from lastfm import *

print(get_charts(SearchType.artists))
print(get_charts(SearchType.tracks))
print(get_charts(SearchType.tracks, geo_filter="si"))
print(get_charts(SearchType.tracks,
                 geo_filter="si",
                 music_type_filter=MusicTypeFilter.electronic,
                 limit=1,
                 year_filter=YearFilter.t2010s))
