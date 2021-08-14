#!/usr/bin/env python3
"""Domain generation algorithm example"""
# https://resources.infosecinstitute.com/domain-generation-algorithm-dga/

import datetime


def generate_domain(year, month, day):
    """Generates a domain by considering the current date."""
    domain = ""

    for _ in range(32):
        year = ((year ^ 8 * year) >> 11) ^ ((year & 0xFFFFFFF0) << 17)
        month = ((month ^ 4 * month) >> 25) ^ 16 * (month & 0xFFFFFFF8)
        day = ((day ^ (day << 13)) >> 19) ^ ((day & 0xFFFFFFFE) << 12)
        domain += chr(((year ^ month ^ day) % 25) + 97)

    # add our own domain
    domain += ".infosec"

    return domain


if __name__ == "__main__":
    NOW = datetime.datetime.now()
    print(generate_domain(NOW.year, NOW.month, NOW.day))
