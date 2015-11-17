#!/usr/bin/env python

"""Get system information"""

import multiprocessing
import six
from psutil import virtual_memory

# http://stackoverflow.com/questions/1006289/how-to-find-out-the-number-of-cpus-using-python
def cpus():
    """Get the number of cpus"""
    six.print_('CPUs: %d' % (multiprocessing.cpu_count()))

# http://stackoverflow.com/questions/22102999/get-total-physical-memory-from-python
def memory():
    """Get the amount of sytem memory"""
    mem = virtual_memory()
    six.print_('Memory: %d' % (mem.total))

if __name__ == '__main__':
    cpus()
    memory()
