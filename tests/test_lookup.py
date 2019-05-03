#!/usr/bin/env python3

import lookup


def test_mst():
    result = lookup.find('www.mst.edu')
    assert result == ('www.mst.edu', '131.151.247.32')


def test_wustl():
    result = lookup.find('www.wustl.edu')
    assert result == ('www.wustl.edu', '128.252.160.5')
