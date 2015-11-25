#!/usr/bin/env python

"""
Demo script for accepting & validating passwords.
"""

import getpass
import hashlib


# https://pymotw.com/2/getpass/
# http://stackoverflow.com/questions/9594125/salt-and-hash-a-password-in-python
def guess():
    """Accept & validate password."""
    curr_pass = getpass.getpass('What is your favorite password? ')
    digest = hashlib.sha1(curr_pass).hexdigest()
    print digest
    if curr_pass.lower() == 'blue':
        print 'Right.  Off you go.'
    else:
        print 'Auuuuugh!'

if __name__ == '__main__':
    guess()
