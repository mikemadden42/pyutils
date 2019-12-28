#!/usr/bin/env python3
"""Compare two directories for conflicts."""

import argparse
import filecmp
import os


def compare(dir1, dir2):
    """Compare two directories for conflicts."""
    cmp = filecmp.dircmp(dir1, dir2)

    print(f"The following directories exist in both {dir1} & {dir2}")
    for conflict in cmp.common_dirs:
        print(conflict)

    print(f"{os.linesep}The following files exist in both {dir1} & {dir2}")
    for conflict in cmp.common_files:
        print(conflict)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description="ping a set of hosts")
    PARSER.add_argument("-f", "--first", help="first directory", required=True)
    PARSER.add_argument("-s", "--second", help="second directory", required=True)
    ARGS = vars(PARSER.parse_args())
    compare(ARGS["first"], ARGS["second"])
