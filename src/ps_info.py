#!/usr/bin/env python3
"""Check various processes."""
# psinfo.py | sort -rnk3 | head

import psutil
import six


def psinfo():
    """Check various processes."""
    for proc in psutil.process_iter(attrs=["username", "pid", "name"]):
        six.print_(proc.name())


if __name__ == "__main__":
    psinfo()
