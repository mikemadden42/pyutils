#!/usr/bin/env python

from nose.tools import assert_tuple_equal

import lookup


def test_mst():
    result = lookup.find('www.mst.edu')
    assert_tuple_equal(result, ('www.mst.edu', '131.151.247.32'))


def test_wustl():
    result = lookup.find('www.wustl.edu')
    assert_tuple_equal(result, ('www.wustl.edu', '128.252.114.30'))
