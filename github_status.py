#!/usr/bin/env python

import requests
import six


def github_status():
    url = "https://status.github.com/api/messages.json"
    response = requests.get(url)
    data = response.json()

    for message in data:
        try:
            six.print_(message['created_on'], message['status'], sep=' - ')
            six.print_(message['body'], end="\n\n")
        except UnicodeEncodeError:
            pass

if __name__ == '__main__':
    github_status()
