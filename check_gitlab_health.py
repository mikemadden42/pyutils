#!/usr/bin/env python3
"""Scan the gitlab logs for any health issues."""

import os
import sys
from collections import defaultdict

import six


def check_shell(logfile):
    """Scan the gitlab nginx logs for any health issues."""
    if not os.path.exists(logfile):
        six.print_(logfile, "does not exist")
        sys.exit()

    warnings = defaultdict(int)
    six.print_("ERRORS IN %s:" % logfile)
    with open(logfile) as infile:
        for line in infile:
            new_line = line.rstrip(os.linesep)
            if new_line.startswith("W, "):
                warning = new_line.split("WARN -- : ")[1]
                warnings[warning] += 1

    for key, val in list(warnings.items()):
        six.print_('"%s" repeated %d times' % (key, val))
    six.print_()


def check_nginx(logfile):
    """Scan the gitlab nginx logs for any health issues."""
    six.print_("ERRORS IN %s:" % logfile)
    with open(logfile) as infile:
        six.print_(infile.read())


if __name__ == "__main__":
    check_shell("/var/log/gitlab/gitlab-shell/gitlab-shell.log")
    check_nginx("/var/log/gitlab/nginx/gitlab_error.log")
