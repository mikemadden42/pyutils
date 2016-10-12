#!/usr/bin/env python
"""Convert UTC to local time."""

# Based on: https://gist.github.com/dmdavis/9670681

from datetime import datetime
from dateutil.tz import tzutc, tzlocal


def utc_local():
    """Convert UTC to local time."""
    utc = datetime.now(tzutc())
    local = utc.astimezone(tzlocal())
    print 'UTC:  ', utc
    print 'Local:', local


if __name__ == '__main__':
    utc_local()
