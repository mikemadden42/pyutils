#!/usr/bin/env python3

import pandas as pd


def list_hosts():
    df = pd.read_csv("lan-hosts.tsv", sep="\t")
    connections = ["Ethernet", "Wi-Fi"]
    for connection in connections:
        print(connection)
        # https://stackoverflow.com/questions/11350770/filter-pandas-dataframe-by-substring-criteria
        conn_df = df[df["Connection"].str.contains(connection)]
        if not conn_df.empty:
            print(conn_df, end="\n\n")

    statuses = ["on", "off"]
    for status in statuses:
        status_df = df[df["Status"].str.contains(status)]
        if not status_df.empty:
            print(status_df, end="\n\n")


if __name__ == "__main__":
    list_hosts()
