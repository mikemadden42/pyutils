#!/usr/bin/env python
"""Remove vowels from words"""

# https://stackoverflow.com/questions/23176001/remove-vowels-from-a-string

import re


def remove_vowels(text):
    """Remove vowels from words"""
    return re.sub("[aeiou]+", "", text)


if __name__ == '__main__':
    BEATS = ('auditbeat', 'filebeat', 'heartbeat', 'journalbeat', 'metricbeat',
             'packetbeat', 'winlogbeat')
    for beat in BEATS:
        print(remove_vowels(beat))
