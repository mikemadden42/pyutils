#!/usr/bin/env python

# https://pymotw.com/2/optparse/
# http://www.alexonlinux.com/pythons-optparse-for-human-beings
# http://superuser.com/questions/501427/gracefully-deleting-files-older-than-30-days
"""
Wrap up tmpwatch to clean up a given directory.
"""

import optparse
import os
import sys
import six


def clean(directory, test_mode):
    """Clean up a given directory."""

    if test_mode:
        six.print_('Running in test mode on %s...' % directory)
        six.print_('tmpwatch -m -t 60d %s' % directory)
    else:
        six.print_('Running in execute mode on %s...' % directory)
        six.print_('tmpwatch -m 60d %s' % directory)


if __name__ == '__main__':
    PARSER = optparse.OptionParser()
    PARSER.add_option('-d', '--directory', dest='directory')
    PARSER.add_option('-t',
                      '--test',
                      dest='test',
                      default=False,
                      action='store_true')

    (OPTIONS, ARGS) = PARSER.parse_args()

    if OPTIONS.directory is None:
        PARSER.print_help()
        sys.exit(os.X_OK)

    clean(OPTIONS.directory, OPTIONS.test)
