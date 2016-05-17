#!/usr/bin/env python
"""Scan the gitlab logs for any health issues."""

import os
from collections import defaultdict


def check_shell(logfile):
    """Scan the gitlab nginx logs for any health issues."""
    warnings = defaultdict(int)
    print 'ERRORS IN %s:' % (logfile)
    with open(logfile) as infile:
        for line in infile:
            line = line.rstrip(os.linesep)
            if line.startswith('W, '):
                warning = line.split('WARN -- : ')[1]
                warnings[warning] += 1

    for key, val in warnings.iteritems():
        print '"%s" repeated %d times' % (key, val)
    print


def check_nginx(logfile):
    """Scan the gitlab nginx logs for any health issues."""
    print 'ERRORS IN %s:' % (logfile)
    with open(logfile) as infile:
        print infile.read()


if __name__ == '__main__':
    check_shell('/var/log/gitlab/gitlab-shell/gitlab-shell.log')
    check_nginx('/var/log/gitlab/nginx/gitlab_error.log')
