#!/usr/bin/env python3
"""Check load."""


import psutil
import six


def load_info():
    """Check disks."""
    try:
        six.print_(psutil.getloadavg())
    except AttributeError as e:
        print(e)


if __name__ == "__main__":
    load_info()
