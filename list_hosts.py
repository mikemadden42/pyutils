#!/usr/bin/env python3

import pandas as pd


def list_hosts():
    df = pd.read_csv("hosts.tsv", sep="\t")
    connections = ["Wired", "2.4G", "5G"]
    for connection in connections:
        print(df[df["Connection Type"] == connection], end="\n\n")


if __name__ == "__main__":
    list_hosts()
