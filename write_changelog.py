#!/usr/bin/env python3
"""Generate YAML changelog"""

import yaml
from nested_dict import nested_dict


def gen_changelog1():
    """Hard code all PRs in dictionary & convert to YAML."""
    dict_file = [
        {
            "pr-1": {
                "meta": {
                    "url": "https://github.com/mikemadden42/hello-changelog/pull/1",
                    "author": "mikemadden42",
                    "hash": "bba923c9b989832ce7b99bfc29d94ba667f5a1b8",
                    "description": "hello python",
                },
                "tags": ["release-highlights"],
            }
        },
        {
            "pr-2": {
                "meta": {
                    "url": "https://github.com/mikemadden42/hello-changelog/pull/1",
                    "author": "mikemadden42",
                    "hash": "bba923c9b989832ce7b99bfc29d94ba667f5a1b8",
                    "description": "hello python",
                },
                "tags": ["release-highlights"],
            }
        },
        {
            "pr-3": {
                "meta": {
                    "url": "https://github.com/mikemadden42/hello-changelog/pull/3",
                    "author": "mikemadden42",
                    "hash": "e6c6efa24c49ae71f13611f9785db9dfa0cc248f",
                    "description": "hello go",
                },
                "tags": ["breaking-changes"],
            }
        },
    ]

    with open(r"changelog.yml", "w") as file:
        yaml.dump(dict_file, file)


# The following classes, functions originated on the following site.
# This allows for multi-line changelog entries.
# https://stackoverflow.com/questions/6432605/any-yaml-libraries-in-python-that-support-dumping-of-long-strings-as-block-liter


class FoldedUnicode(str):
    pass


class LiteralUnicode(str):
    pass


def folded_unicode_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=">")


def literal_unicode_representer(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")


yaml.add_representer(FoldedUnicode, folded_unicode_representer)
yaml.add_representer(LiteralUnicode, literal_unicode_representer)


def gen_changelog2():
    """Define all PRs in nested dictionary & convert to YAML."""
    changelog = nested_dict()
    changelog["pr-1"]["meta"]["author"] = "mikemadden42"
    changelog["pr-1"]["meta"]["description"] = "hello python"
    changelog["pr-1"]["meta"]["hash"] = "472ab8cb35800f5a228bdb55ef6c792ced3d6e6b"
    changelog["pr-1"]["meta"][
        "url"
    ] = "https://github.com/mikemadden42/hello-changelog/pull/1"
    changelog["pr-1"]["changelog"] = "break(packetbeat): add java example"
    changelog["pr-1"]["meta"]["tags"] = ["release-highlights", "breaking-change"]

    changelog["pr-2"]["meta"]["author"] = "mikemadden42"
    changelog["pr-2"]["meta"]["description"] = "hello rust"
    changelog["pr-2"]["meta"]["hash"] = "42e46bdcbd95fc187fe29b0be4e9bf6403a638c6"
    changelog["pr-2"]["meta"][
        "url"
    ] = "https://github.com/mikemadden42/hello-changelog/pull/2"
    changelog["pr-2"]["changelog"] = "break(packetbeat): add java example"
    changelog["pr-2"]["meta"]["tags"] = ["breaking-change"]

    changelog["pr-3"]["meta"]["author"] = "mikemadden42"
    changelog["pr-3"]["meta"]["description"] = "hello go"
    changelog["pr-3"]["meta"]["hash"] = "04fcab4a7e9ccfa98ea3e7ee33c192caa5731ae0"
    changelog["pr-3"]["meta"][
        "url"
    ] = "https://github.com/mikemadden42/hello-changelog/pull/3"
    changelog["pr-3"]["changelog"] = LiteralUnicode(
        "break(packetbeat): add java example\nfix(functionbeat, journalbeat):hello java"
    )
    changelog["pr-3"]["meta"]["tags"] = ["backport"]

    with open(r"changelog.yml", "w") as file:
        yaml.dump(changelog.to_dict(), file)


if __name__ == "__main__":
    gen_changelog2()
