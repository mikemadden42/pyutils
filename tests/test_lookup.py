#!/usr/bin/env python3

import lookup


def test_mst():
    result = lookup.find("www.mst.edu")
    assert result == ("www.mst.edu", "131.151.247.32")


def test_wustl():
    result = lookup.find("www.wustl.edu")
    assert result == ("www.wustl.edu", "128.252.160.5")


def test_umsl():
    result = lookup.find("www.umsl.edu")
    assert result == ("www.umsl.edu", "134.124.1.234")


def test_slu():
    result = lookup.find("www.slu.edu")
    assert result == ("www.slu.edu", "165.134.206.195")
