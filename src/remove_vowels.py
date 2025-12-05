#!/usr/bin/env python3
"""Remove vowels from words"""

# https://stackoverflow.com/questions/23176001/remove-vowels-from-a-string

import re

import six


def remove_vowels(text):
    """Remove vowels from words"""
    return re.sub("[aeiou]+", "", text)


if __name__ == "__main__":
    BEATS = (
        "auditbeat",
        "filebeat",
        "heartbeat",
        "journalbeat",
        "metricbeat",
        "packetbeat",
        "winlogbeat",
    )
    for beat in BEATS:
        six.print_(remove_vowels(beat))
