#!/usr/bin/env python

# https://mail.python.org/pipermail/tutor/2003-August/024435.html
# https://docs.python.org/2/library/collections.html#ordereddict-objects
"""
Get the stats (ips, urls, agents) for an Apache access log.
"""

import os
import sys
import six

try:
    from collections import OrderedDict
except ImportError:
    six.print_('python 2.7.x needed')
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

        # six.print_(IPS)
        # six.print_(URLS)
        # six.print_(AGENTS)

        six.print_(OrderedDict(sorted(list(URLS.items()), key=lambda t: t[1])))


if __name__ == '__main__':
    visitors()
