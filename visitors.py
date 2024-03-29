#!/usr/bin/env python3

# https://mail.python.org/pipermail/tutor/2003-August/024435.html
# https://docs.python.org/2/library/collections.html#ordereddict-objects
"""
Get the stats (ips, urls, agents) for an Apache access log.
"""

import os
from collections import OrderedDict

import six

IPS = {}
URLS = {}
AGENTS = {}


def visitors():
    """Get the stats for an Apache access log."""

    try:
        with open("access.log", "r") as log:
            for line in log:
                new_line = line.rstrip(os.linesep)
                stats = new_line.split("^")
                IPS[stats[3]] = IPS.setdefault(stats[3], 0) + 1
                URLS[stats[8]] = URLS.setdefault(stats[8], 0) + 1
                AGENTS[stats[9]] = AGENTS.setdefault(stats[9], 0) + 1

            # six.print_(IPS)
            # six.print_(URLS)
            # six.print_(AGENTS)

            six.print_(OrderedDict(sorted(list(URLS.items()), key=lambda t: t[1])))
    except IOError:
        print("File", "access.log", "not found")


if __name__ == "__main__":
    visitors()
