#!/usr/bin/env python3
"""Find empty directories."""

# http://stackoverflow.com/questions/26774892/how-to-find-recursively-empty-directories-in-python

import os
import six


def empty_dirs(root_dir='.'):
    """Find empty directories."""
    six.print_(root_dir)
    for dirpath, dirs, files in os.walk(root_dir):
        if not dirs and not files:
            yield dirpath


if __name__ == '__main__':
    six.print_(list(empty_dirs('/tmp')))
    six.print_(list(empty_dirs('/var/tmp')))
