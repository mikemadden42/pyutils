#!/usr/bin/env python3.4

import requests

def most_popular():
    url = "http://gdata.youtube.com/feeds/api/standardfeeds/most_popular?alt=json"
    response = requests.get(url)
    data = response.json()

    for video in data['feed']['entry'][0:10]:
        try:
            print((video['title']['$t']))
        except UnicodeEncodeError:
            pass

if __name__ == '__main__':
    most_popular()
