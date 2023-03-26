#!/usr/bin/env python

import sysinfo


def test_cores():
    # Ensure there is at least 1 core.
    result = sysinfo.get_cores()
    assert result >= 1


def test_memory():
    # Ensure there is at least 512 MB.
    result = sysinfo.get_memory()
    MIN_RAM = 536870912
    assert result >= MIN_RAM
