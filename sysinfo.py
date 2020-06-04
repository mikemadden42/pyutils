#!/usr/bin/env python3
"""Get system information"""

import datetime
import multiprocessing

import psutil
import six

# http://stackoverflow.com/questions/12400256/python-converting-epoch-time-into-the-datetime


def boot():
    """Get the boot time"""
    bootup = psutil.boot_time()
    time_stamp = datetime.datetime.fromtimestamp(bootup).strftime("%Y-%m-%d %H:%M:%S")
    six.print_("Boot time: %s" % time_stamp)


# http://stackoverflow.com/questions/1006289/how-to-find-out-the-number-of-cpus-using-python


def get_cores():
    """Get the number of CPU cores"""
    return multiprocessing.cpu_count()


def cpus():
    """Get the number of cpus"""
    six.print_("Total CPUs: %d" % get_cores())
    try:
        six.print_("Load averages: %f %f %f" % psutil.getloadavg())
        six.print_("Physical CPUs: %d" % psutil.cpu_count(logical=False))
        six.print_("Logical CPUs: %d" % psutil.cpu_count())
        six.print_("CPU current freq: %d Mhz" % psutil.cpu_freq().current)
        six.print_("CPU min freq: %d Mhz" % psutil.cpu_freq().min)
        six.print_("CPU max freq: %d Mhz" % psutil.cpu_freq().max)
    except AttributeError:
        pass


def get_memory():
    """Get the amount of memory"""
    return psutil.virtual_memory().total


# https://stackoverflow.com/questions/12523586/python-format-size-application-converting-b-to-kb-mb-gb-tb/52379087
SIZE_UNITS = ["B", "KB", "MB", "GB", "TB", "PB"]


def get_readable_file_size(size_in_bytes):
    """Get humable friendly size"""
    index = 0
    while size_in_bytes >= 1024:
        size_in_bytes /= 1024
        index += 1
    try:
        return f"{size_in_bytes} {SIZE_UNITS[index]}"
    except IndexError:
        return "File too large"


# http://stackoverflow.com/questions/22102999/get-total-physical-memory-from-python


def memory():
    """Get the amount of sytem memory"""
    six.print_("Memory: %s" % get_readable_file_size(get_memory()))


def disks():
    """Get the amount of disk space"""
    parts = psutil.disk_partitions()
    for part in parts:
        six.print_(
            "Mount: %s %f%% full"
            % (part.mountpoint, psutil.disk_usage(part.mountpoint).percent)
        )


if __name__ == "__main__":
    boot()
    cpus()
    memory()
    disks()
