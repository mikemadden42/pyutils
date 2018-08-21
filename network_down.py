#!/usr/bin/env python
"""sqlite demo"""

import datetime
import platform
import sqlite3

import psutil


def main():
    """sqlite demo"""
    address = psutil.net_if_addrs()['en0'][0].address
    date = str(datetime.datetime.now())
    host = platform.node()
    mac = psutil.net_if_addrs()['en0'][1].address

    conn = sqlite3.connect("network.sqlite")
    cursor = conn.cursor()

    sql_create = "CREATE TABLE outages (date text, device text, ip text, mac text)"
    sql_insert = "INSERT INTO outages VALUES ('{}', '{}', '{}', '{}')".format(
        date, host, address, mac)

    try:
        cursor.execute(sql_create)
    except sqlite3.OperationalError as ex:
        print(ex)

    cursor.execute(sql_insert)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
