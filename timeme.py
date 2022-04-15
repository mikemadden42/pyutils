#!/usr/bin/env python3
"""Hello world function"""

import os
import sys
import time
from functools import wraps


def timeit(method):
    """Decorator to measure and compare the execution time"""

    @wraps(method)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = method(*args, **kwargs)
        end_time = time.time()
        print(f"{method.__name__} => {(end_time-start_time)*1000} ms")

        return result

    return wrapper


def hello():
    """Hello world function"""
    if os.name == "posix":
        print(f"Hello uid {os.getuid()} on {sys.platform}.")
    else:
        print(f"Hello on {sys.platform}.")


if __name__ == "__main__":
    hello()
