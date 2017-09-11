#!/usr/bin/env python
"""Check various processes."""
# psinfo.py | sort -rnk3 | head

import psutil
import six

def psinfo():
    """Check various processes."""
    for proc in psutil.process_iter():
        if proc.username() != 'root' and proc.username() != 'swbuild':
            six.print_(proc.username(), proc.name(), proc.memory_info().rss)


if __name__ == '__main__':
    psinfo()
