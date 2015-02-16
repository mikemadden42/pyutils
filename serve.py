#!/usr/bin/env python

# Based on https://github.com/Nakiami/MultithreadedSimpleHTTPServer
# Works for both Python 2.x & Python 3.x

from six.moves import BaseHTTPServer
from six.moves import SimpleHTTPServer
from six.moves import socketserver

import os
import sys


class ThreadingSimpleServer(socketserver.ThreadingMixIn, BaseHTTPServer.HTTPServer):
    pass

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

if sys.argv[2:]:
    os.chdir(sys.argv[2])

server = ThreadingSimpleServer(('', port), SimpleHTTPServer.SimpleHTTPRequestHandler)

try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print("Finished")
