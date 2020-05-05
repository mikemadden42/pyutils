#!/usr/bin/env python

import sysinfo


def test_cores():
    # Ensure there is at least 2 cores.
    result = sysinfo.get_cores()
    assert result >= 2


def test_memory():
    # Ensure there is at least 4 GB.
    result = sysinfo.get_memory()
    assert result >= 1073741824
