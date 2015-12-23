#!/usr/bin/env python

# http://stackoverflow.com/questions/12497901/i-need-python-to-process-all-files-in-a-directory-but-it-only-gets-one
# http://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
# https://docs.python.org/2/library/shutil.html
"""Split a large directory into smaller directories"""

import os
import shutil


def split_dir(directory):
    """Split a large directory into smaller directories"""

    files = os.listdir(directory)
    size = len(files)

    batches = int(size / 100)
    i = 0

    while i <= batches:
        os.mkdir(directory + '/' + str(i))
        start = i * 100
        end = i * 100 + 100
        part = files[start:end]

        for part_file in part:
            shutil.move(directory + '/' + part_file, directory + '/' + str(i))

        i += 1


if __name__ == '__main__':
    split_dir('nma1')
    split_dir('nma2')
