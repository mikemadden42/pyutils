#!/usr/bin/env python3
"""
Demo script for accepting & validating passwords.
"""

import getpass
import hashlib
import six

# https://pymotw.com/2/getpass/
# http://stackoverflow.com/questions/9594125/salt-and-hash-a-password-in-python


def guess():
    """Accept & validate password."""

    curr_pass = getpass.getpass('What is your favorite password? ')
    digest = hashlib.sha1(curr_pass.encode('utf-8')).hexdigest()
    six.print_(digest)
    if curr_pass.lower() == 'blue':
        six.print_('Right.  Off you go.')
    else:
        six.print_('Auuuuugh!')


if __name__ == '__main__':
    guess()
