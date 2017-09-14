#!/usr/bin/env python
"""Check swap."""

import psutil
import six


def swap_info():
    """Check swap."""
    print psutil.swap_memory()


if __name__ == '__main__':
    swap_info()
