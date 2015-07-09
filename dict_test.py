#!/usr/bin/env python

"""Test various dictionary sorts"""

import six
import sys

try:
    from collections import OrderedDict
except ImportError:
    six.print_('python 2.7.x needed')
    sys.exit(1)


def dict_test():
    """Test various dictionary sorts"""
    fruit = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
    six.print_(fruit)

    # dictionary sorted by key
    six.print_(OrderedDict(sorted(list(fruit.items()), key=lambda t: t[0])))

    # dictionary sorted by value
    six.print_(OrderedDict(sorted(list(fruit.items()), key=lambda t: t[1])))

    # dictionary sorted by length of the key string
    six.print_(OrderedDict(sorted(list(fruit.items()), key=lambda t: len(t[0]))))

if __name__ == '__main__':
    dict_test()
