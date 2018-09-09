#!/usr/bin/env python3
"""Get the current NFL scores in json"""

import requests

# https://code.google.com/p/nfl-game-stats/
# http://www.nfl.com/liveupdate/scorestrip/ss.json
# http://www.nfl.com/liveupdate/scorestrip/postseason/ss.xml


def nfl_scores():
    """Get the current NFL scores"""

    url = 'http://www.nfl.com/liveupdate/scores/scores.json'
    response = requests.get(url)
    data = response.json()

    for key in data:
        print(data[key]['home']['abbr'], data[key]['home']['score']['T'],
              data[key]['away']['abbr'], data[key]['away']['score']['T'])


if __name__ == '__main__':
    nfl_scores()
