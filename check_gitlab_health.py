#!/usr/bin/env python
"""Scan the gitlab logs for any health issues."""

import os
from collections import defaultdict
import six


def check_shell(logfile):
    """Scan the gitlab nginx logs for any health issues."""
    warnings = defaultdict(int)
    six.print_('ERRORS IN %s:' % (logfile))
    with open(logfile) as infile:
        for line in infile:
            line = line.rstrip(os.linesep)
            if line.startswith('W, '):
                warning = line.split('WARN -- : ')[1]
                warnings[warning] += 1

    for key, val in warnings.iteritems():
        six.print_('"%s" repeated %d times' % (key, val))
    six.print_()


def check_nginx(logfile):
    """Scan the gitlab nginx logs for any health issues."""
    six.print_('ERRORS IN %s:' % (logfile))
    with open(logfile) as infile:
        six.print_(infile.read())


if __name__ == '__main__':
    check_shell('/var/log/gitlab/gitlab-shell/gitlab-shell.log')
    check_nginx('/var/log/gitlab/nginx/gitlab_error.log')
