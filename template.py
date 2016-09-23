#!/usr/bin/env python
"""Hello world function"""

import os
import sys


def hello():
    """Hello world function"""
    print 'Hello %s on %s.' % (os.getlogin(), sys.platform)


if __name__ == '__main__':
    hello()
