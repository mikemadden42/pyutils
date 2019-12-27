#!/usr/bin/env python3
"""Check load."""

import os

import six


def load_info():
    """Check disks."""
    six.print_(os.getloadavg())


if __name__ == "__main__":
    load_info()
