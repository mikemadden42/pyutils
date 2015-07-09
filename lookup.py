#!/usr/bin/env python

"""Perform a DNS lookup for a set of hosts."""

import six
import socket
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import cpu_count


def find(host):
    """Perform a DNS lookup for a given host."""
    try:
        ip_address = socket.gethostbyname(host)
        return(host, ip_address)
    except socket.error as msg:
        six.print_(host, msg)


def lookup():
    """Perform a DNS lookup for a set of hosts."""
    infile = open('hosts.txt', 'r')
    urls = [x.strip() for x in infile.readlines()]

    pool = ThreadPool(cpu_count() * 4)
    results = pool.map(find, urls)

    for result in results:
        if result is not None:
            six.print_(result)

    pool.close()
    pool.join()

if __name__ == '__main__':
    lookup()
