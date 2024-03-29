#!/usr/bin/env python3
"""sqlite demo"""

import datetime
import platform
import sqlite3
import sys

import psutil
import six


def main():
    """sqlite demo"""
    try:
        address = psutil.net_if_addrs()["en0"][0].address
    except KeyError as error:
        six.print_("Unable to find network interface", error, flush=True)
        sys.exit(1)
    date = str(datetime.datetime.now())
    host = platform.node()
    mac = psutil.net_if_addrs()["en0"][1].address

    conn = sqlite3.connect("network.sqlite")
    cursor = conn.cursor()

    sql_create = "CREATE TABLE outages (date text, device text, ip text, mac text)"
    sql_insert = "INSERT INTO outages VALUES ('{}', '{}', '{}', '{}')".format(
        date, host, address, mac
    )

    try:
        cursor.execute(sql_create)
    except sqlite3.OperationalError as ex:
        six.print_(ex, flush=True)

    cursor.execute(sql_insert)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
