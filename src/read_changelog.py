#!/usr/bin/env python3
"""Read yml example"""

import yaml


def read_changelog():
    """Read interim changelog file."""
    try:
        with open(r"changelog.yml") as file:
            changelog = yaml.safe_load(file)

            for change in changelog:
                print(change)
                print("- author:", changelog[change]["meta"]["author"])
                print("- description:", changelog[change]["meta"]["description"])
                print("- hash:", changelog[change]["meta"]["hash"])
                print("- url:", changelog[change]["meta"]["url"])
                print("- tags:", changelog[change]["meta"]["tags"])
                print("- changelog:", changelog[change]["changelog"])
    except FileNotFoundError as error:
        print(error)


if __name__ == "__main__":
    read_changelog()
