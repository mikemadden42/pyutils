#!/usr/bin/env python3
"""Check if anything is listening on port 22."""

import socket
from contextlib import closing

# https://stackoverflow.com/questions/19196105/how-to-check-if-a-network-port-is-open-on-linux


def check_socket(host, port):
    """Check if anything is listening on provided port."""
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        sock.settimeout(4)
        if sock.connect_ex((host, port)) == 0:
            print("Port", port, "is open")
        else:
            print("Port", port, "is not open")


check_socket("localhost", 22)
