#!/usr/bin/env python3
"""Read yml example"""

import yaml


def read_changelog():
    """Read interum changelog file."""
    with open(r"changelog.yml") as file:
        prs = yaml.safe_load(file)

        for pr in prs:
            print(pr)
            print("- author:", prs[pr]["meta"]["author"])
            print("- description:", prs[pr]["meta"]["description"])
            print("- hash:", prs[pr]["meta"]["hash"])
            print("- url:", prs[pr]["meta"]["url"])
            print("- tags:", prs[pr]["meta"]["tags"])
            print("- changelog:", prs[pr]["changelog"])


if __name__ == "__main__":
    read_changelog()
