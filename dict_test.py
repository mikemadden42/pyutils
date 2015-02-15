#!/usr/bin/env python

from collections import OrderedDict


def dict_test():
    d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
    print(d)

    # dictionary sorted by key
    print(OrderedDict(sorted(list(d.items()), key=lambda t: t[0])))

    # dictionary sorted by value
    print(OrderedDict(sorted(list(d.items()), key=lambda t: t[1])))

    # dictionary sorted by length of the key string
    print(OrderedDict(sorted(list(d.items()), key=lambda t: len(t[0]))))

if __name__ == '__main__':
    dict_test()
