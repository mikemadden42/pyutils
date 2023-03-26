#!/usr/bin/env python3

import datetime

import countdown


def test_birthdays():
    start = datetime.date(2011, 11, 30)
    end = datetime.date(2013, 11, 8)
    result = countdown.diff_dates(start, end)
    EXPECTED_VALUE=709
    assert result == EXPECTED_VALUE


def test_homerun_records():
    start = datetime.date(1961, 10, 1)
    end = datetime.date(1998, 9, 8)
    result = countdown.diff_dates(start, end)
    EXPECTED_RESULT = 13491
    assert result == EXPECTED_RESULT


def test_independence_day():
    start = datetime.date(1776, 7, 4)
    end = datetime.date(2016, 7, 4)
    result = countdown.diff_dates(start, end)
    EXPECTED_RESULT = 87658
    assert result == EXPECTED_RESULT


def test_market_crashes():
    start = datetime.date(1929, 10, 29)
    end = datetime.date(1987, 10, 19)
    result = countdown.diff_dates(start, end)
    EXPECTED_RESULT = 21174
    assert result == EXPECTED_RESULT


def test_superbowls():
    start = datetime.date(1967, 1, 15)
    end = datetime.date(2016, 2, 7)
    result = countdown.diff_dates(start, end)
    EXPECTED_RESULT = 17920
    assert result == EXPECTED_RESULT
