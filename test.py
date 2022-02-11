from lastfm import *

print(get_charts(ChartType.artists))
print(get_charts(ChartType.tracks))
print(get_charts(ChartType.tracks, geo_filter="si"))
print(get_charts(ChartType.tracks,
                 geo_filter="si",
                 music_type_filter=MusicTypeFilter.electronic,
                 limit=1,
                 year_filter=YearFilter.t2010s))
