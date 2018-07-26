#!/usr/bin/env python3
"""Get the current NFL scores in json"""

import requests
import six

# https://code.google.com/p/nfl-game-stats/
# http://www.nfl.com/liveupdate/scorestrip/ss.json
# http://www.nfl.com/liveupdate/scorestrip/postseason/ss.xml


def nfs_scores():
    """Get the current NFL scores"""

    url = 'http://www.nfl.com/liveupdate/scorestrip/ss.json'
    response = requests.get(url)
    data = response.json()

    week = data['w']
    year = data['y']
    six.print_('%d WEEK %d' % (year, week))
    for game in data['gms']:
        try:
            six.print_(game['h'], game['hs'], game['v'], game['vs'])
        except UnicodeEncodeError:
            pass


if __name__ == '__main__':
    nfs_scores()
