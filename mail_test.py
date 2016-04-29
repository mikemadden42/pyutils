#!/usr/bin/env python
"""Simple SMTP test that sends an email"""

# https://docs.python.org/2/library/smtplib.html

import smtplib
import six

from six.moves import input


def prompt(message):
    """Simple prompt method"""
    return input(message).strip()


def mail_test():
    """Simple SMTP test"""
    fromaddr = prompt("From: ")
    toaddrs = prompt("To: ").split()
    six.print_("Enter message, end with ^D (Unix) or ^Z (Windows):")

    # Add the From: and To: headers at the start!
    msg = ("From: %s\r\nTo: %s\r\n\r\n" % (fromaddr, ", ".join(toaddrs)))
    while 1:
        try:
            line = input()
        except EOFError:
            break
        if not line:
            break
        msg = msg + line

    six.print_("Message length is " + repr(len(msg)))

    server = smtplib.SMTP('localhost')
    server.set_debuglevel(1)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


if __name__ == '__main__':
    mail_test()