#!/usr/bin/env python

"""Check URLs with a JSON endpoint"""

import os
import requests


def check_urls():
    """Check URLs with a JSON endpoint"""
    with open('json_urls.txt', 'r') as infile:
        for url in infile:
            url = url.rstrip(os.linesep)
            try:
                data = requests.get(url)
                print(data.json())
            except ValueError as msg:
                print(('FAIL:', url, data.status_code, msg))

if __name__ == '__main__':
    check_urls()
