#!/usr/bin/env python3
"""Create /etc/hosts file from hostnames."""

import socket

import six


def make_hosts():
    """Create /etc/hosts file from hostnames."""
    infile = open('hosts.txt', 'r')
    hosts = [x.strip() for x in infile.readlines()]
    for host in hosts:
        try:
            ip_address = socket.gethostbyname(host)
            six.print_('%-15s %s' % (ip_address, host))
        except socket.error as msg:
            six.print_('# %s %s' % (host, msg))


if __name__ == '__main__':
    make_hosts()
