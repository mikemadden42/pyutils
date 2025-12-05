#!/usr/bin/env python3
"""Threading example."""

import concurrent.futures
import logging
import time


def thread_function(name):
    """Threading example."""
    logging.info("Batter %s: up", name)
    time.sleep(2)
    logging.info("Batter %s: out", name)


if __name__ == "__main__":
    logging.basicConfig(
        datefmt="%H:%M:%S",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    lineup = [
        "Wong",
        "Edman",
        "Goldschmidt",
        "DeJong",
        "Carpenter",
        "Molina",
        "Fowler",
        "O'Neill",
        "Bader",
    ]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, lineup)
