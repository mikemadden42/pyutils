#!/usr/bin/env python3
"""Print recent quakes."""

import time

import requests
import six


def quakes():
    """Print recent quakes."""
    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"
    req = requests.get(url, timeout=10)
    data = req.json()
    for feature in data["features"]:
        date = time.strftime(
            "%Y-%m-%d %H:%M:%S", time.gmtime(feature["properties"]["time"] / 1000.0)
        )
        kind = feature["properties"]["type"]
        mag = feature["properties"]["mag"]
        place = feature["properties"]["place"]
        depth = feature["geometry"]["coordinates"][2]
        six.print_(date, kind, mag, place, depth)


if __name__ == "__main__":
    quakes()
