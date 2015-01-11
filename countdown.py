#!/usr/bin/env python3.4

# http://stackoverflow.com/questions/8419564/difference-between-two-dates

from datetime import date


def diff_dates(date1, date2):
    return abs(date2 - date1).days


def main():
    d1 = date(2013, 1, 1)
    d2 = date(2013, 9, 13)
    result1 = diff_dates(d2, d1)
    print('{} days between {} and {}'.format(result1, d1, d2))

main()
