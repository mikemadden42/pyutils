#!/usr/bin/env python3
"""Count the number of 1s in a binary representation of a number."""

import six


def hamming(i):
    """Count the number of 1s in a binary representation of a number."""
    return bin(i).count("1")


if __name__ == "__main__":
    six.print_(hamming(0x5555555555555555))
