#!/usr/bin/env python3

import lookup


def test_mst():
    result = lookup.find("www.mst.edu")
    assert result == ("www.mst.edu", "131.151.247.20")


def test_wustl():
    result = lookup.find("www.wustl.edu")
    assert result == ("www.wustl.edu", "23.185.0.3")


def test_umsl():
    result = lookup.find("www.umsl.edu")
    assert result == ("www.umsl.edu", "134.124.1.234")


def test_google_dns():
    result = lookup.find("google-public-dns-a.google.com.")
    assert result == ("google-public-dns-a.google.com.", "8.8.8.8")
