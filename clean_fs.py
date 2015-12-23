#!/usr/bin/env python

# https://pymotw.com/2/optparse/
# http://www.alexonlinux.com/pythons-optparse-for-human-beings
# http://superuser.com/questions/501427/gracefully-deleting-files-older-than-30-days

"""
Wrap up tmpwatch to clean up a given directory.
"""

import optparse
import os
import six
import sys


def clean(directory, test_mode):
    """Clean up a given directory."""

    if test_mode:
        six.print_('Running in test mode on %s...' % directory)
        six.print_('tmpwatch -m -t 60d %s' % directory)
    else:
        six.print_('Running in execute mode on %s...' % directory)
        six.print_('tmpwatch -m 60d %s' % directory)


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-d', '--directory', dest='directory')
    parser.add_option('-t', '--test', dest='test', default=False,
                      action='store_true')

    (options, args) = parser.parse_args()

    if options.directory is None:
        parser.print_help()
        sys.exit(os.EX_USAGE)

    clean(options.directory, options.test)
