#!/usr/bin/env python3

import csv

from rich import print


def read_csv(filename):
    with open("data.csv", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names: {", ".join(row)}\n')
            print(f'Title: {row["Title"]}')
            print(f'URL: {row["URL"]}')
            print(f'Username: {row["Username"]}')
            if len(row["Password"]) < 12:
                print(f'Password: [bold red]{row["Password"]}[/bold red]')
            else:
                print(f'Password: {row["Password"]}')
            print()
            line_count += 1
        print(f"Processed {line_count} lines.")


if __name__ == "__main__":
    read_csv("data.csv")
