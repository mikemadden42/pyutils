#!/usr/bin/env python3
"""Show unanswered posts in discuss.elastic.co"""

import requests


def unanswered(page=1):
    """Show unanswered posts in discuss.elastic.co"""
    req = requests.get(
        "https://discuss.elastic.co/c/elastic-stack/beats/l/latest.json?page="
        + str(page),
        timeout=10,
    )
    print("========")
    for topic in req.json()["topic_list"]["topics"]:
        if topic["posts_count"] == 1:
            print(topic["created_at"], topic["title"])
    print("========")


if __name__ == "__main__":
    for p in range(8):
        unanswered(p)
