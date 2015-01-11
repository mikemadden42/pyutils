#!/usr/bin/env python3.4

import os
import socket


def lookup():
    with open('hosts.txt', 'r') as f:
        for host in f:
            host = host.rstrip(os.linesep)
            try:
                ip = socket.gethostbyname(host)
                print(host, ip)
            except socket.error as msg:
                print(host, msg)

if __name__ == '__main__':
    lookup()
