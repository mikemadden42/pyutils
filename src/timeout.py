#!/usr/bin/env python3

# https://majornetwork.net/2022/04/handling-retries-in-python-requests/

import time

import requests
import urllib3
from requests.adapters import HTTPAdapter
from urllib3 import Retry


def timeout():
    print(urllib3.__version__)
    session = requests.Session()
    # backoff factor of 1 for the retry delay (the formula for the delay is
    # {backoff factor} * (2 ** ({retry number} - 1)), except that the first
    # retry is always immediate)
    adapter = HTTPAdapter(
        max_retries=Retry(
            total=5,
            backoff_factor=1,
            allowed_methods=None,
            status_forcelist=[429, 500, 502, 503, 504],
        )
    )
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    start_time = time.monotonic()
    try:
        r = session.get("http://httpbin.org/status/503")
        # Do something useful with r.
        print(r)
    except Exception as e:
        print(type(e))
        print(e)

    stop_time = time.monotonic()
    print(round(stop_time - start_time, 2), "seconds")


if __name__ == "__main__":
    timeout()
