#!/usr/bin/env python3
'''Check if packages exist for Raspbian.'''

from collections import defaultdict
import gzip
import os
import urllib
import six


def check(pkgs):
    '''Check if packages exist for Raspbian.'''
    packages = defaultdict(int)
    required_pkgs = 'required_pkgs.txt'
    url = 'http://tinyurl.com/yaljokp8'

    if not os.path.exists(pkgs):
        six.print_('Downloading package list...')
        urllib.urlretrieve(url, pkgs)

    with gzip.open(pkgs, 'rt') as pkgfile:
        for line in pkgfile:
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
    check('Packages.gz')
