#!/usr/bin/env python
"""Count the number of 1s in a binary representation of a number."""


def hamming(i):
    """Count the number of 1s in a binary representation of a number."""
    return bin(i).count('1')


if __name__ == '__main__':
    print hamming(0x5555555555555555)
