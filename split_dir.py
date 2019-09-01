#!/usr/bin/env python3

# http://stackoverflow.com/questions/12497901/i-need-python-to-process-all-files-in-a-directory-but-it-only-gets-one
# http://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
# https://docs.python.org/2/library/shutil.html
"""Split a large directory into smaller directories"""

import argparse
import os
import shutil


def split_dir(directory, n):
    """Split a large directory into smaller directories"""

    files = os.listdir(directory)
    size = len(files)

    batches = int(size / n)
    i = 0

    while i <= batches:
        os.mkdir(directory + "/" + str(i))
        start = i * n
        end = i * n + n
        part = files[start:end]

        for part_file in part:
            shutil.move(directory + "/" + part_file, directory + "/" + str(i))

        i += 1


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description="split up a large directory")
    PARSER.add_argument("-d", "--directory", help="directory", required=True)
    PARSER.add_argument("-n", "--number", help="number", required=True)
    ARGS = vars(PARSER.parse_args())
    split_dir(ARGS["directory"], int(ARGS["number"]))
