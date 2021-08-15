#!/usr/bin/env python3

# https://gist.github.com/dropmeaword/9372cbeb29e8390521c2
# https://github.com/kcp18/browserhistory
# https://geekswipe.net/technology/computing/analyze-chromes-browsing-history-with-python/
# https://pythonexamples.org/python-sqlite3-delete-all-rows-from-table/

import sqlite3


def list_history():
    try:
        conn = sqlite3.connect("History")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT url, title, datetime((last_visit_time/1000000)-11644473600, 'unixepoch', 'localtime') AS last_visit_time FROM urls ORDER BY last_visit_time DESC"
        )
        urls = cursor.fetchall()
        for url in urls:
            print(url)
    except sqlite3.OperationalError as err:
        print("Ensure Chrome is not running:", err)
    cursor.close()
    conn.close()


if __name__ == "__main__":
    list_history()
