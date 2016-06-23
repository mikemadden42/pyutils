#!/usr/bin/env python
'''Check if packages exist for Raspbian.'''

from collections import defaultdict
import gzip
import os
import urllib
import six


def check():
    '''Check if packages exist for Raspbian.'''
    packages = defaultdict(int)
    all_pkgs = 'all_pkgs.gz'
    required_pkgs = 'required_pkgs.txt'
    url = 'http://reflection.oss.ou.edu/raspbian/raspbian/dists/jessie/main/binary-armhf/Packages.gz'

    if not os.path.exists(all_pkgs):
        six.print_('Downloading package list...')
        urllib.urlretrieve(url, all_pkgs)

    with gzip.open(all_pkgs, 'rt') as pkgs:
        for line in pkgs:
            line = line.rstrip(os.linesep)
            if line.startswith('Package'):
                pkg = line.split(': ')[1]
                packages[pkg] += 1

    with open(required_pkgs, 'rt') as required:
        for line in required:
            line = line.rstrip(os.linesep)
            if line not in packages:
                six.print_(line)


if __name__ == '__main__':
    check()
