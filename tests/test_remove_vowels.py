#!/usr/bin/env python

import remove_vowels


def test_auditbeat():
    result = remove_vowels.remove_vowels("auditbeat")
    assert result == "dtbt"


def test_filebeat():
    result = remove_vowels.remove_vowels("filebeat")
    assert result == "flbt"


def test_heartbeat():
    result = remove_vowels.remove_vowels("heartbeat")
    assert result == "hrtbt"


def test_journalbeat():
    result = remove_vowels.remove_vowels("journalbeat")
    assert result == "jrnlbt"


def test_metricbeat():
    result = remove_vowels.remove_vowels("metricbeat")
    assert result == "mtrcbt"


def test_packetbeat():
    result = remove_vowels.remove_vowels("packetbeat")
    assert result == "pcktbt"


def test_winlogbeat():
    result = remove_vowels.remove_vowels("winlogbeat")
    assert result == "wnlgbt"
