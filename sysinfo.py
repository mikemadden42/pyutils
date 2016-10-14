#!/usr/bin/env python
"""Get system information"""

import datetime
import multiprocessing
import psutil
import six

# http://stackoverflow.com/questions/12400256/python-converting-epoch-time-into-the-datetime


def boot():
    """Get the boot time"""

    bootup = psutil.boot_time()
    time_stamp = \
        datetime.datetime.fromtimestamp(bootup).strftime('%Y-%m-%d %H:%M:%S')
    six.print_('Boot time: %s' % time_stamp)


# http://stackoverflow.com/questions/1006289/how-to-find-out-the-number-of-cpus-using-python


def cpus():
    """Get the number of cpus"""

    six.print_('Total CPUs: %d' % multiprocessing.cpu_count())
    try:
        six.print_('Physical CPUs: %d' % psutil.cpu_count(logical=False))
        six.print_('Logical CPUs: %d' % psutil.cpu_count())
    except AttributeError:
        pass


# http://stackoverflow.com/questions/22102999/get-total-physical-memory-from-python


def memory():
    """Get the amount of sytem memory"""

    mem = psutil.virtual_memory()
    six.print_('Memory: %d' % mem.total)


if __name__ == '__main__':
    boot()
    cpus()
    memory()
