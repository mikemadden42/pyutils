#!/usr/bin/env python

"""
Get the stats (ips, urls, agents) for an Apache access log.
"""

# https://mail.python.org/pipermail/tutor/2003-August/024435.html
# https://docs.python.org/2/library/collections.html#ordereddict-objects

import os
import sys

try:
    from collections import OrderedDict
except ImportError:
    print('python 2.7.x needed')
    sys.exit(1)

IPS = {}
URLS = {}
AGENTS = {}


def visitors():
    """Get the stats for an Apache access log."""
    with open('access.log', 'r') as log:
        for line in log:
            line = line.rstrip(os.linesep)
            stats = line.split('^')
            IPS[stats[3]] = IPS.setdefault(stats[3], 0) + 1
            URLS[stats[8]] = URLS.setdefault(stats[8], 0) + 1
            AGENTS[stats[9]] = AGENTS.setdefault(stats[9], 0) + 1

        # print(IPS)
        # print(URLS)
        # print(AGENTS)

        # print(OrderedDict(sorted(list(IPS.items()), key=lambda t: t[1])))
        print(OrderedDict(sorted(list(URLS.items()), key=lambda t: t[1])))
        # print(OrderedDict(sorted(list(AGENTS.items()), key=lambda t: t[1])))


if __name__ == '__main__':
    visitors()
