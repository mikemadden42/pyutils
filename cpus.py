#!/usr/bin/env python

"""Get the number of cpus"""

# http://stackoverflow.com/questions/1006289/how-to-find-out-the-number-of-cpus-using-python

import multiprocessing
import six


def cpus():
    """Get the number of cpus"""
    six.print_('CPUs: %d' % (multiprocessing.cpu_count()))

if __name__ == '__main__':
    cpus()
