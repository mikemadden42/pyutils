#!/usr/bin/env python3
"""Test various dictionary sorts"""

from collections import OrderedDict
import six


def dict_test():
    """Test various dictionary sorts"""

    fruit = {"banana": 3, "apple": 4, "pear": 1, "orange": 2}
    six.print_(fruit)

    # dictionary sorted by key
    six.print_(OrderedDict(sorted(list(fruit.items()), key=lambda t: t[0])))

    # dictionary sorted by value
    six.print_(OrderedDict(sorted(list(fruit.items()), key=lambda t: t[1])))

    # dictionary sorted by length of the key string
    six.print_(OrderedDict(sorted(list(fruit.items()), key=lambda t: len(t[0]))))


if __name__ == "__main__":
    dict_test()
