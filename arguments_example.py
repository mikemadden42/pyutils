#!/usr/bin/env python3
"""Argument example program"""

import os
import sys


def test_args(greeting, *argv):
    """Argument example function"""
    # https://www.geeksforgeeks.org/args-kwargs-python/
    # https://en.wikipedia.org/wiki/Variadic_function#In_Python
    if os.name == "posix":
        for name in argv:
            print(f"{greeting} uid {os.getuid()} from {name} on {sys.platform}.")
    else:
        for name in argv:
            print(f"{greeting} {name} on {sys.platform}.")


if __name__ == "__main__":
    test_args("Hello", "Jimi", "Ringo")
    test_args("Bye", "BA", "Face")
