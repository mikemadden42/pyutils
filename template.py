#!/usr/bin/env python
"""Hello world function"""

from __future__ import print_function

import os
import sys

import six


def hello():
    """Hello world function"""
    six.print_('Hello uid %s on %s.' % (os.getuid(), sys.platform))


if __name__ == '__main__':
    hello()
