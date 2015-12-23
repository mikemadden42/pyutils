#!/usr/bin/env python

# http://stackoverflow.com/questions/8419564/difference-between-two-dates

"""Get the difference between two dates"""

import datetime
import six


def diff_dates(date1, date2):
    """Get the difference between two dates"""

    return abs(date2 - date1).days


if __name__ == '__main__':
    START_DATE = datetime.date(2015, 8, 19)
    NOW = datetime.datetime.now()
    END_DATE = datetime.date(NOW.year, NOW.month, NOW.day)
    RESULT1 = diff_dates(END_DATE, START_DATE)
    six.print_(RESULT1)
