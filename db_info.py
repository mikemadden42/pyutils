#!/usr/bin/env python3

# https://stackoverflow.com/questions/305378/list-of-tables-db-schema-dump-etc-using-the-python-sqlite3-api

import argparse
import os.path
import sqlite3


def parse_args():
    """Get the command line arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="database file", required=True)
    return parser.parse_args()


def db_info(db_file):
    db_filename = db_file
    newline_indent = "\n   "

    if os.path.exists(db_filename):
        try:
            db = sqlite3.connect(db_filename)
            db.text_factory = str
            cur = db.cursor()

            result = cur.execute(
                "SELECT name FROM sqlite_master WHERE type='table';"
            ).fetchall()
            table_names = sorted(list(zip(*result, strict=True))[0])
            print("\ntables are:" + newline_indent + newline_indent.join(table_names))

            for table_name in table_names:
                result = cur.execute("PRAGMA table_info('%s')" % table_name).fetchall()
                column_names = list(zip(*result, strict=True))[1]
                print(
                    ("\ncolumn names for %s:" % table_name)
                    + newline_indent
                    + (newline_indent.join(column_names))
                )
        except sqlite3.OperationalError as err:
            print("Please close all chrome instances:", err)
            print("Error database info:", err)

        db.close()
    else:
        print(f"Error: file {db_filename} does not exist.")


if __name__ == "__main__":
    args = parse_args()
    db_info(args.file)
