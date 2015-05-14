#!/usr/bin/env python

# https://mail.python.org/pipermail/tutor/2003-August/024435.html
# https://docs.python.org/2/library/collections.html#ordereddict-objects

import os
import sys

try:
    from collections import OrderedDict
except ImportError:
    print('python 2.7.x needed')
    sys.exit(1)

ips = {}
urls = {}
agents = {}


def visitors():
    with open('access.log', 'r') as f:
        for line in f:
            line = line.rstrip(os.linesep)
            stats = line.split('^')
            ips[stats[3]] = ips.setdefault(stats[3], 0) + 1
            urls[stats[8]] = urls.setdefault(stats[8], 0) + 1
            agents[stats[9]] = agents.setdefault(stats[9], 0) + 1

        # print(ips)
        # print(urls)
        # print(agents)

        # print(OrderedDict(sorted(list(ips.items()), key=lambda t: t[1])))
        print(OrderedDict(sorted(list(urls.items()), key=lambda t: t[1])))
        # print(OrderedDict(sorted(list(agents.items()), key=lambda t: t[1])))


if __name__ == '__main__':
        visitors()
