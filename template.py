#!/usr/bin/env python3
"""Hello world function"""

from __future__ import print_function

import os
import sys

import six


def hello():
    """Hello world function"""
    if os.name == 'posix':
        six.print_('Hello uid %s on %s.' % (os.getuid(), sys.platform))
    else:
        six.print_('Hello on %s.' % (sys.platform))


if __name__ == '__main__':
    hello()
