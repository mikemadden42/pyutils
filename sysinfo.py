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
    return multiprocessing.cpu_count()


def cpus():
    """Get the number of cpus"""

    six.print_("Total CPUs: %d" % get_cores())
    try:
        six.print_("Physical CPUs: %d" % psutil.cpu_count(logical=False))
        six.print_("Logical CPUs: %d" % psutil.cpu_count())
    except AttributeError:
        pass


def get_memory():
    return psutil.virtual_memory().total


# http://stackoverflow.com/questions/22102999/get-total-physical-memory-from-python


def memory():
    """Get the amount of sytem memory"""

    six.print_("Memory: %d" % get_memory())


if __name__ == "__main__":
    boot()
    cpus()
    memory()
