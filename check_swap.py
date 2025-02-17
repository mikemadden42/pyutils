#!/usr/bin/env python3
"""Check swap usage & send alert if swap is high."""

import platform
import smtplib

import six


def mail_alert(percent):
    """Send alert if swap is high."""
    subject = "swap on %s - %.2f used" % (platform.node(), percent)
    sender = "from@fastmail.com"
    receivers = "to@fastmail.com"

    message = "Subject: %s\r\nFrom: %s\r\nTo: %s\r\n\r\n" % (subject, sender, receivers)
    try:
        server = smtplib.SMTP("localhost")
        server.sendmail(sender, receivers, message)
        six.print_("Successfully sent email")
    except smtplib.SMTPException:
        six.print_("Error: unable to send email")


def check_swap():
    """Check swap usage."""
    threshold = 0.20
    try:
        with open("/proc/swaps") as infile:
            next(infile)
            for line in infile:
                stats = line.split()
                size = stats[2]
                used = stats[3]
                percent_used = float(used) / float(size)
                if percent_used > threshold:
                    mail_alert(percent_used)
    except IOError:
        print("File", "/proc/swaps", "not found")


if __name__ == "__main__":
    check_swap()
