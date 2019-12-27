#!/usr/bin/env python3
"""
Demo script for reading YAML.
"""

import six
import yaml

# http://martin-thoma.com/configuration-files-in-python/


def read_yaml():
    """Read & print YAML."""

    with open("config.yml", "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)

        for section in cfg:
            six.print_(section)
            six.print_(cfg["mysql"])
            six.print_(cfg["other"])


if __name__ == "__main__":
    read_yaml()
