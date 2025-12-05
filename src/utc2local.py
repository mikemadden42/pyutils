#!/usr/bin/env python3
"""Convert UTC to local time."""

# Based on: https://gist.github.com/dmdavis/9670681

from datetime import datetime

import six
from dateutil.tz import tzlocal, tzutc


def utc_local():
    """Convert UTC to local time."""
    utc = datetime.now(tzutc())
    local = utc.astimezone(tzlocal())
    six.print_("UTC:  ", utc)
    six.print_("Local:", local)


if __name__ == "__main__":
    utc_local()
