#!/usr/bin/env python3
"""Compare two directories for conflicts."""

import filecmp

import six


def compare(dir1, dir2):
    """Compare two directories for conflicts."""
    six.print_("The following directories exist in both:", dir1, dir2)
    for conflict in filecmp.dircmp(dir1, dir2).common_dirs:
        six.print_(conflict)

    six.print_("\nThe following files exist in both:", dir1, dir2)
    for conflict in filecmp.dircmp(dir1, dir2).common_files:
        six.print_(conflict)


if __name__ == "__main__":
    compare("/etc", "/etc")
