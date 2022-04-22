#!/usr/bin/env python3
"""List items in slack."""

# https://github.com/os/slacker
# https://api.slack.com/methods

import os

import six
from slacker import Slacker


def list_slack():
    """List channels & users in slack."""
    try:
        token = os.environ["SLACK_TOKEN"]
        slack = Slacker(token)

        # Get channel list
        response = slack.channels.list()
        channels = response.body["channels"]
        for channel in channels:
            six.print_(channel["id"], channel["name"])
            # if not channel['is_archived']:
            # slack.channels.join(channel['name'])
        six.print_()

        # Get users list
        response = slack.users.list()
        users = response.body["members"]
        for user in users:
            if not user["deleted"]:
                six.print_(user["id"], user["name"], user["is_admin"], user["is_owner"])
        six.print_()
    except KeyError as ex:
        six.print_("Environment variable %s not set." % str(ex))


if __name__ == "__main__":
    list_slack()
