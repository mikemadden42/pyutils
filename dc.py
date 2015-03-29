#!/usr/bin/env python

import socket
import sys


def dc():
    host = 'www.alamo.ca'

    try:
        ip = socket.gethostbyname(host)
    except socket.error as msg:
        print(host, msg)
        sys.exit(1)

    if ip.startswith('65'):
        print('ETC')
    elif ip.startswith('12'):
        print('PTC')
    else:
        print('UNKNOWN')


if __name__ == '__main__':
    dc()
