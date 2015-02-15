#!/usr/bin/env python

# Based on https://github.com/Nakiami/MultithreadedSimpleHTTPServer
# Works for both Python 2 & Python 3

try:
    import SocketServer
except ImportError:
    import socketserver
try:
    import BaseHTTPServer
    import SimpleHTTPServer
except ImportError:
    import http.server
import os
import sys

try:
    class ThreadingSimpleServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
        pass
except NameError:
    class ThreadingSimpleServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
        pass

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

if sys.argv[2:]:
    os.chdir(sys.argv[2])

try:
    server = ThreadingSimpleServer(('', port), http.server.SimpleHTTPRequestHandler)
except NameError:
    server = ThreadingSimpleServer(('', port), SimpleHTTPServer.SimpleHTTPRequestHandler)

try:
    while 1:
        sys.stdout.flush()
        server.handle_request()
except KeyboardInterrupt:
    print("Finished")
