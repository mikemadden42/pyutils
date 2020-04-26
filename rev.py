#!/usr/bin/env python
"""Reverse a string."""


def rev(s):
    """Reverse a string."""
    # https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python
    # The slice statement means start at string length, end at position 0,
    # move with the step -1 (or one step backward).
    return s[::-1]


if __name__ == "__main__":
    print(rev("Hello world!"))
