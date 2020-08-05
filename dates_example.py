#!/usr/bin/env python3
"""Example date program"""

from datetime import date, timedelta


def dates():
    """Example date function"""
    now = date.today()
    one_month_ago = now - timedelta(days=30)
    two_months_ago = now - timedelta(days=60)
    three_months_ago = now - timedelta(days=90)
    two_weeks_ago = now - timedelta(weeks=2)
    one_week_ago = now - timedelta(weeks=1)
    print(f"today: {now}")
    print(f"one_month_ago: {one_month_ago}")
    print(f"two_months_ago: {two_months_ago}")
    print(f"three_months_ago: {three_months_ago}")
    print(f"two_weeks_ago: {two_weeks_ago}")
    print(f"one_week_ago: {one_week_ago}")


if __name__ == "__main__":
    dates()
