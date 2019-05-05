#!/usr/bin/env python3
"""Check disks."""

import psutil
import six


def disk_info():
    """Check disks."""
    for part in psutil.disk_partitions():
        mount = part.mountpoint
        percent = psutil.disk_usage(mount).percent
        six.print_(mount, percent)


if __name__ == "__main__":
    disk_info()
