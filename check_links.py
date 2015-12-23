#!/usr/bin/env python

"""Find broken links in a directory"""

import os


def check_links(directory):
    """Find broken links in a directory"""

    files = os.listdir(directory)
    for filename in files:
        full_path = os.path.join(directory, filename)
        if not os.path.exists(full_path):
            print full_path


if __name__ == '__main__':
    check_links('/etc/alternatives')
    check_links('/usr/bin')
