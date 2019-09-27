#!/usr/bin/env python
"""check elastic"""

from __future__ import print_function

import argparse
import requests
from requests.auth import HTTPBasicAuth


def elastic_check(server):
    """check elastic"""
    url = "https://" + server + ":9200/_cluster/health"
    req = requests.get(url, auth=HTTPBasicAuth("elastic", "********"), verify=False)
    j = req.json()
    print(j["status"])


def email_alert(recipient, subject, body):
    """send email alert"""
    print(recipient, subject, body)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description="check elastic cluster")
    PARSER.add_argument("-s", "--server", help="elastic server", required=True)
    ARGS = vars(PARSER.parse_args())
    elastic_check(ARGS["server"])
