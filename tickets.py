#!/usr/bin/env python3
"""Summarize tickets by user"""

from collections import defaultdict
import argparse
import csv
import six


def tickets(tickets_file):
    """Summarize tickets by user"""
    items = defaultdict(list)

    with open(tickets_file, 'rb') as infile:
        reader = csv.reader(infile)
        for row in reader:
            assignee = row[49]
            summary = row[32]
            request = row[50]
            date = row[19]
            work_details = '%s - %s - %s' % (request, date, summary)
            items[assignee].append(work_details)

    for (key, values) in items.items():
        six.print_(key, '-', len(values), 'request(s)')
        for item in values:
            six.print_(item)
        six.print_()


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description='summarize a set of tickets')
    PARSER.add_argument('-f', '--file', help='tickets file', required=True)
    ARGS = vars(PARSER.parse_args())
    tickets(ARGS['file'])
