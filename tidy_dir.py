#!/usr/bin/env python3
"""
Simple script that organizes a large directory that contains
many individual files. The files will be moved to a directory
named after the first letter of the file name.
"""

import os
import shutil


def tidy_dir(directory):
    """Organizes a large directory with many files."""

    dir_list = os.listdir(directory)
    os.chdir(directory)

    for filename in dir_list:
        first_letter = filename[0].lower()
        if not os.path.isdir(first_letter):
            os.mkdir(first_letter)
        shutil.move(filename, first_letter)


if __name__ == '__main__':
    tidy_dir('dvds')
