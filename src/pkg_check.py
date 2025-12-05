#!/usr/bin/env python3
"""Check if packages exist for Raspbian."""

import gzip
import os
import sys
from collections import defaultdict
from urllib.parse import urlparse

import six


def check(pkgs):
    """Check if packages exist for Raspbian."""
    packages = defaultdict(int)
    required_pkgs = "required_pkgs.txt"
    url = "https://debian.osuosl.org/debian/dists/buster/main/binary-amd64/Packages.gz"

    url_data = urlparse(url)
    if not url_data.scheme.startswith("file"):
        if not os.path.exists(pkgs):
            six.print_("Downloading package list...", flush=True)
            six.moves.urllib.request.urlretrieve(url, pkgs)
    else:
        print(f"Invalid URL: {url}")
        sys.exit(1)

    with gzip.open(pkgs, "rt") as pkg_file:
        for line in pkg_file:
            new_line = line.rstrip(os.linesep)
            if new_line.startswith("Package"):
                pkg = new_line.split(": ")[1]
                packages[pkg] += 1

    with open(required_pkgs, "rt") as required:
        for line in required:
            new_line = line.rstrip(os.linesep)
            if new_line not in packages:
                six.print_(new_line, flush=True)


if __name__ == "__main__":
    check("Packages.gz")
