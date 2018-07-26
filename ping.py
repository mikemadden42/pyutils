#!/usr/bin/env python3
"""Perform a ping for a set of hosts."""

import argparse
try:
    import commands as cmds
except ImportError as ex:
    import subprocess as cmds
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import cpu_count
import six


def find(host):
    """Perform a ping for a given host."""

    cmd = 'ping -w 1 -q ' + host
    (status, text) = cmds.getstatusoutput(cmd)
    return (status, host, text)


def ping(hosts):
    """Perform a ping for a set of hosts."""

    infile = open(hosts, 'r')
    hosts = [x.strip() for x in infile.readlines()]

    pool = ThreadPool(cpu_count() * 4)
    results = pool.map(find, hosts)

    for result in results:
        if result[0] != 0:
            six.print_(result[1])

    pool.close()
    pool.join()


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description='ping a set of hosts')
    PARSER.add_argument('-f', '--file', help='hosts file', required=True)
    ARGS = vars(PARSER.parse_args())
    ping(ARGS['file'])
