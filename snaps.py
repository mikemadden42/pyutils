#!/usr/bin/env python3
"""Randomly pick snap words."""

import secrets


def snaps():
    """Randomly pick snap words."""
    snap_words = ["begin", "great", "suddenly", "before", "enough", "probably"]
    print(secrets.choice(snap_words))


if __name__ == "__main__":
    snaps()
