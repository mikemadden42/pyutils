#!/usr/bin/env python

"""Get the amount of sytem memory"""

# http://stackoverflow.com/questions/22102999/get-total-physical-memory-from-python

import six
from psutil import virtual_memory


def memory():
    """Get the amount of sytem memory"""
    mem = virtual_memory()
    six.print_(mem.total)

if __name__ == '__main__':
    memory()
