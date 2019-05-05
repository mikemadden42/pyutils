#!/usr/bin/env python3
"""Post slack message."""

# https://github.com/os/slacker
# https://api.slack.com/methods

import os
import six
from slacker import Slacker


def post_slack():
    """Post slack message."""
    try:
        token = os.environ["SLACK_TOKEN"]
        slack = Slacker(token)

        obj = slack.chat.post_message(
            channel="#bots",
            text="",
            as_user=True,
            attachments=[{"pretext": "pretext", "text": "text"}],
        )
        six.print_(
            obj.successful, obj.__dict__["body"]["channel"], obj.__dict__["body"]["ts"]
        )
    except (KeyError) as ex:
        six.print_("Environment variable %s not set." % str(ex))


if __name__ == "__main__":
    post_slack()
