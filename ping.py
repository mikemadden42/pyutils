#!/usr/bin/env python
"""Perform a ping for a set of hosts."""

import commands
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import cpu_count
import six


def find(host):
    """Perform a ping for a given host."""

    cmd = 'ping -c 1 -q ' + host
    (status, text) = commands.getstatusoutput(cmd)
    return (status, host, text)


def ping():
    """Perform a ping for a set of hosts."""

    infile = open('hosts.txt', 'r')
    hosts = [x.strip() for x in infile.readlines()]

    pool = ThreadPool(cpu_count() * 4)
    results = pool.map(find, hosts)

    for result in results:
        if result[0] != 0:
            six.print_(result[1])

    pool.close()
    pool.join()


if __name__ == '__main__':
    ping()
