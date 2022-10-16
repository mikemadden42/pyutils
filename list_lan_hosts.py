#!/usr/bin/env python3

import pandas as pd


def list_hosts():
    df = pd.read_csv("lan-hosts.tsv", sep="\t")
    connections = ["Ethernet", "Wi-Fi"]
    for connection in connections:
        print(df[df["Connection"] == connection], end="\n\n")

    statuses = ["on", "off"]
    for status in statuses:
        print(df[df["Status"] == status], end="\n\n")


if __name__ == "__main__":
    list_hosts()
