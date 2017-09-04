#!/usr/bin/env python
"""Print recent quakes."""

import time
import requests


def quakes():
    """Print recent quakes."""
    url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
    req = requests.get(url)
    data = req.json()
    for feature in data['features']:
        date = time.strftime('%Y-%m-%d %H:%M:%S',
                             time.gmtime(
                                 feature['properties']['time'] / 1000.0))
        kind = feature['properties']['type']
        mag = feature['properties']['mag']
        place = feature['properties']['place']
        depth = feature['geometry']['coordinates'][2]
        print date, kind, mag, place, depth


if __name__ == '__main__':
    quakes()
