#!/usr/bin/env python3
"""Logging example"""

import logging


def logging_example():
    """Logging example"""
    logging.basicConfig(
        filemode="w",
        filename="app.log",
        format="%(asctime)s|%(name)s|%(levelname)s|%(message)s",
        level=logging.INFO,
    )

    # The debug message will not be logged since the level is info.
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")
    logging.critical("This is a critical message")


if __name__ == "__main__":
    logging_example()
