#!/usr/bin/env python3
"""Get the current NFL scores in json"""

import sys

import requests
import simplejson
import six

# https://code.google.com/p/nfl-game-stats/
# http://www.nfl.com/liveupdate/scorestrip/ss.json
# http://www.nfl.com/liveupdate/scorestrip/postseason/ss.xml


def nfl_scores():
    """Get the current NFL scores"""

    url = "http://www.nfl.com/liveupdate/scores/scores.json"
    response = requests.get(url)
    try:
        data = response.json()
    except simplejson.errors.JSONDecodeError as error:
        six.print_("Error decoding JSON:")
        six.print_(error)
        sys.exit(1)

    for key in data:
        six.print_(
            data[key]["home"]["abbr"],
            data[key]["home"]["score"]["T"],
            data[key]["away"]["abbr"],
            data[key]["away"]["score"]["T"],
        )


if __name__ == "__main__":
    nfl_scores()
