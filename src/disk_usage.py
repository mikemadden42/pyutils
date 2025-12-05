#!/usr/bin/env python3
"""Estimate file space usage."""

# Based on https://gist.github.com/xamox/4711286

import os
import sys
from collections import namedtuple

import six


def disk_partitions(all_mounts=False):
    """Return all mountd partitions as a nameduple.
    If all_mounts == False return physical partitions only."""
    phydevs = []
    disk_ntuple = namedtuple("partition", "device mountpoint fstype")
    try:
        fsys = open("/proc/filesystems", "r")
        for line in fsys:
            if not line.startswith("nodev"):
                phydevs.append(line.strip())
    except IOError:
        print("File", "/proc/filesystems", "not found")
        sys.exit(os.EX_OSFILE)

    retlist = []
    mtab = open("/etc/mtab", "r")
    for line in mtab:
        if not all_mounts and line.startswith("none"):
            continue
        fields = line.split()
        device = fields[0]
        mountpoint = fields[1]
        fstype = fields[2]
        if not all_mounts and fstype not in phydevs:
            continue
        if device == "none":
            device = ""
        ntuple = disk_ntuple(device, mountpoint, fstype)
        retlist.append(ntuple)
    return retlist


def disk_usage(path):
    """Return disk usage associated with path."""
    stats = os.statvfs(path)
    free = stats.f_bavail * stats.f_frsize
    total = stats.f_blocks * stats.f_frsize
    used = (stats.f_blocks - stats.f_bfree) * stats.f_frsize
    usage_ntuple = namedtuple("usage", "total used free percent")
    try:
        percent = (float(used) / total) * 100
    except ZeroDivisionError:
        percent = 0
    # NB: the percentage is -5% than what shown by df due to
    # reserved blocks that we are currently not considering:
    # http://goo.gl/sWGbH
    return usage_ntuple(total, used, free, round(percent, 1))


if __name__ == "__main__":
    for part in disk_partitions():
        six.print_(part)
        six.print_("    %s\n" % str(disk_usage(part.mountpoint)))
