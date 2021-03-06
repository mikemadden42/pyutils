#!/usr/bin/env python3

# Based on https://github.com/Nakiami/MultithreadedSimpleHTTPServer
# Works for both Python 2.x & Python 3.x
"""Simple HTTP server"""

import os
import sys

import six
from six.moves import BaseHTTPServer, SimpleHTTPServer, socketserver


class ThreadingSimpleServer(socketserver.ThreadingMixIn, BaseHTTPServer.HTTPServer):
    """Simple HTTP server"""


if sys.argv[1:]:
    PORT = int(sys.argv[1])
else:
    PORT = 8000

if sys.argv[2:]:
    os.chdir(sys.argv[2])

SERVER = ThreadingSimpleServer(("", PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

try:
    while 1:
        sys.stdout.flush()
        SERVER.handle_request()
except KeyboardInterrupt:
    six.print_("Finished")
