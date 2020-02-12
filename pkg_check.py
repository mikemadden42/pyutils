#!/usr/bin/env python3
"""Check if packages exist for Raspbian."""

import gzip
import os
import sys
from collections import defaultdict

import six
import six.moves


def check(pkgs):
    """Check if packages exist for Raspbian."""
    packages = defaultdict(int)
    required_pkgs = "required_pkgs.txt"
    url = "http://debian.uchicago.edu/debian/dists/buster/main/binary-amd64/Packages.gz"

    if url.lower().startswith("http"):
        if not os.path.exists(pkgs):
            six.print_("Downloading package list...")
            six.moves.urllib.request.urlretrieve(url, pkgs)
    else:
        print(f"Invalid URL: {url}")
        sys.exit(1)

    with gzip.open(pkgs, "rt") as pkgfile:
        for line in pkgfile:
            line = line.rstrip(os.linesep)
            if line.startswith("Package"):
                pkg = line.split(": ")[1]
                packages[pkg] += 1

    with open(required_pkgs, "rt") as required:
        for line in required:
            line = line.rstrip(os.linesep)
            if line not in packages:
                six.print_(line)


if __name__ == "__main__":
    check("Packages.gz")
