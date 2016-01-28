#!/usr/bin/env python
"""Summarize tickets by user"""

from collections import defaultdict
import argparse
import csv


def tickets(tickets_file):
    """Summarize tickets by user"""
    d = defaultdict(list)

    with open(tickets_file, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            assignee = row[49]
            summary = row[32]
            request = row[50]
            date = row[19]
            work_details = '%s - %s - %s' % (request, date, summary)
            d[assignee].append(work_details)

    for (key, values) in d.iteritems():
        print key, '-', len(values), 'request(s)'
        for item in values:
            print item
        print


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description='summarize a set of tickets')
    PARSER.add_argument('-f', '--file', help='tickets file', required=True)
    ARGS = vars(PARSER.parse_args())
    tickets(ARGS['file'])
