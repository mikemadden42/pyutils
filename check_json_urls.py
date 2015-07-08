#!/usr/bin/env python

import os
import requests


def check_urls():
    with open('json_urls.txt', 'r') as f:
        for url in f:
            url = url.rstrip(os.linesep)
            try:
                r = requests.get(url)
                print(r.json())
            except ValueError as msg:
                print(('FAIL:', url, r.status_code, msg))

if __name__ == '__main__':
        check_urls()
