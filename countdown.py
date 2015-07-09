#!/usr/bin/env python

"""Get the difference between two dates"""

# http://stackoverflow.com/questions/8419564/difference-between-two-dates

import six
from datetime import date


def diff_dates(date1, date2):
    """Get the difference between two dates"""
    return abs(date2 - date1).days


if __name__ == '__main__':
    START_DATE = date(2013, 1, 1)
    END_DATE = date(2013, 9, 13)
    RESULT1 = diff_dates(END_DATE, START_DATE)
    six.print_(RESULT1)
