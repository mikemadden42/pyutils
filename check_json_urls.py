#!/usr/bin/env python

import requests


def check_urls():
    with open('urls.txt', 'r') as f:
        for url in f:
            try:
                r = requests.get(url)
                print((r.json()))
            except ValueError as msg:
                print(('FAIL:', url, r.status_code))

if __name__ == '__main__':
        check_urls()
