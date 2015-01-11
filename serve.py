#!/usr/bin/env python3.4

# Based on https://github.com/Nakiami/MultithreadedSimpleHTTPServer
# Updated for Python 3

import http.server
import os
import socketserver
import sys


class ThreadingSimpleServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

if sys.argv[2:]:
    os.chdir(sys.argv[2])

server = ThreadingSimpleServer(('', port), http.server.SimpleHTTPRequestHandler)
try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print("Finished")
