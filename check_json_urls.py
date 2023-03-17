#!/usr/bin/env python3
"""Check URLs with a JSON endpoint"""

import os

import requests
import six


def check_urls():
    """Check URLs with a JSON endpoint"""

    with open("json_urls.txt", "r") as infile:
        for url in infile:
            url = url.rstrip(os.linesep)
            try:
                data = requests.get(url, timeout=10)
                six.print_(data.json())
            except ValueError as msg:
                six.print_(("FAIL:", url, data.status_code, msg))


if __name__ == "__main__":
    check_urls()
