#!/usr/bin/env python3
"""Check load and email alert if load is high."""

import multiprocessing
import platform
import smtplib

import six


def mail_alert(load):
    """Email alert if load is high."""
    subject = "load on %s -> %.2f" % (platform.node(), load)
    sender = "from@fastmail.com"
    receivers = "to@fastmail.com"

    message = "Subject: %s\r\nFrom: %s\r\nTo: %s\r\n\r\n" % (subject, sender, receivers)
    try:
        server = smtplib.SMTP("localhost")
        server.sendmail(sender, receivers, message)
        six.print_("Successfully sent email")
    except smtplib.SMTPException:
        six.print_("Error: unable to send email")


def check_load():
    """Check load."""
    try:
        with open("/proc/loadavg") as infile:
            for line in infile:
                stats = line.split()
                load_avg = float(stats[2])
                if load_avg > multiprocessing.cpu_count():
                    mail_alert(load_avg)
    except IOError:
        print("File", "/proc/loadavg", "not found")


if __name__ == "__main__":
    check_load()
