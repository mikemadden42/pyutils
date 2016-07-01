#!/usr/bin/env python

import platform
import smtplib


def mail_alert(percent):
    subject = 'swap on %s - %.2f used' % (platform.node(), percent)
    sender = 'from@fastmail.com'
    receivers = 'to@fastmail.com'

    message = ("Subject: %s\r\nFrom: %s\r\nTo: %s\r\n\r\n" %
               (subject, sender, receivers))
    try:
        smtpObj = smtplib.SMTP('localhost')
        smtpObj.sendmail(sender, receivers, message)
        print "Successfully sent email"
    except smtplib.SMTPException:
        print "Error: unable to send email"


def check_swap():
    with open('/proc/swaps') as f:
        next(f)
        for line in f:
            stats = line.split()
            size = stats[2]
            used = stats[3]
            percent_used = float(used) / float(size)
            if percent_used > 0.20:
                mail_alert(percent_used)


if __name__ == '__main__':
    check_swap()
