#!/usr/bin/env python3
"""Compare two directories for conflicts."""

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
    compare("/etc", "/etc")
