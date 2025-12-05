#!/usr/bin/env python3
"""Hello world function"""

import json

# https://www.programiz.com/python-programming/json


def pretty_json():
    """Hello world function"""
    person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

    # Getting dictionary
    person_dict = json.loads(person_string)

    # Pretty Printing JSON string back
    print(json.dumps(person_dict, indent=4, sort_keys=True))


if __name__ == "__main__":
    pretty_json()
