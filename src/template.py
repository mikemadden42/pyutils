#!/usr/bin/env python3
"""Hello world function"""

import os
import sys


def hello():
    """Hello world function"""
    if os.name == "posix":
        print(f"Hello uid {os.getuid()} on {sys.platform}.")
    else:
        print(f"Hello on {sys.platform}.")


if __name__ == "__main__":
    hello()
