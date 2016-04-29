#!/usr/bin/env python

import datetime
from nose.tools import eq_

import countdown


def test_birthdays():
    start = datetime.date(2011, 11, 30)
    end = datetime.date(2013, 11, 8)
    result = countdown.diff_dates(start, end)
    eq_(result, 709)


def test_homerun_records():
    start = datetime.date(1961, 10, 1)
    end = datetime.date(1998, 9, 8)
    result = countdown.diff_dates(start, end)
    eq_(result, 13491)


def test_independence_day():
    start = datetime.date(1776, 7, 4)
    end = datetime.date(2016, 7, 4)
    result = countdown.diff_dates(start, end)
    eq_(result, 87658)


def test_market_crashes():
    start = datetime.date(1929, 10, 29)
    end = datetime.date(1987, 10, 19)
    result = countdown.diff_dates(start, end)
    eq_(result, 21174)


def test_superbowls():
    start = datetime.date(1967, 1, 15)
    end = datetime.date(2016, 2, 7)
    result = countdown.diff_dates(start, end)
    eq_(result, 17920)
