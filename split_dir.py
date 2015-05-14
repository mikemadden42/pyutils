#!/usr/bin/env python

# http://stackoverflow.com/questions/12497901/i-need-python-to-process-all-files-in-a-directory-but-it-only-gets-one
# http://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
# https://docs.python.org/2/library/shutil.html

import os
import shutil
import sys


def split_dir(d):
    files = os.listdir(d)
    size = len(files)

    batches = size / 100
    i = 0

    while i <= batches:
        os.mkdir(d + '/' + str(i))
        start = i * 100
        end = (i * 100) + 100
        part = files[start:end]

        for f in part:
            shutil.move(d + '/' + f, d + '/' + str(i))

        i += 1

if __name__ == '__main__':
    split_dir('nma1')
    split_dir('nma2')
