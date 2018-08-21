#!/usr/bin/env python
"""sqlite demo"""

import datetime
import platform
import sqlite3


def main():
    """sqlite demo"""
    host = platform.node()
    date = str(datetime.datetime.now())

    print(date)
    print(host)

    conn = sqlite3.connect('network.sqlite')
    cursor = conn.cursor()

    # date format - YYYY-MM-DD HH:MM:SS.SSS
    sql_create = """
    CREATE TABLE outages
    (date text, device text, ip text)
    """

    sql_insert = """
    INSERT INTO outages
    VALUES ('2018-08-21 13:04:52', 'localhost', '127.0.0.1')
    """

    try:
        cursor.execute(sql_create)
    except sqlite3.OperationalError as ex:
        print(ex)

    cursor.execute(sql_insert)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
