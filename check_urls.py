#!/usr/bin/env python

import os
import requests


def check():
    with open('urls.txt', 'r') as f:
        for url in f:
            url = url.rstrip(os.linesep)

            try:
                r = requests.get(url)
            except Exception, e:
                print(url, e)
                continue

            if (r.status_code != requests.codes.ok) or (len(r.content) == 0):
                print(url)

if __name__ == '__main__':
    check()
