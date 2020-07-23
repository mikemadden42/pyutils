#!/usr/bin/env python3
"""Hello world function"""

import secrets


def rand_int():
    """Generate int between 0 and 100."""
    while True:
        yield secrets.randbelow(100)


def main():
    """Demo for random number generator."""
    # Print out 8 random numbers.
    gen = rand_int()
    for i in range(8):
        print(next(gen))

    # Print out random numbers forever.
    for i in rand_int():
        print(i)


if __name__ == "__main__":
    main()
