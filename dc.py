#!/usr/bin/env python

"""
Get the location of a data center based on ip address.
ETC ip addresses start with a 65.
PTC ip addresses start with a 12.
"""

import six
import socket
import sys


def location():
    """Get the location of a data center based on ip address."""

    host = 'www.alamo.ca'

    try:
        ip_address = socket.gethostbyname(host)
    except socket.error, msg:
        six.print_(host, msg)
        sys.exit(1)

    if ip_address.startswith('65'):
        six.print_('ETC')
    elif ip_address.startswith('12'):
        six.print_('PTC')
    else:
        six.print_('UNKNOWN')


if __name__ == '__main__':
    location()
