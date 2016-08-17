#!/usr/bin/env python
"""Upload a file to slack."""

# https://github.com/os/slacker
# https://api.slack.com/methods

import os
from slacker import Slacker


def upload_slack(file_upload):
    """Upload a file to slack."""
    try:
        token = os.environ['SLACK_TOKEN']
        slack = Slacker(token)

        # By default all newly-uploaded files are private and only visible to
        # the owner. They become public once they are shared into a public
        # channel (which can happen at upload time via the channels argument).
        # obj = slack.files.upload(file_upload, channels='#general')
        obj = slack.files.upload(file_upload)
        print obj.successful, obj.body['file']['channels'], obj.body['file'][
            'id']
    except KeyError, ex:
        print 'Environment variable %s not set.' % str(ex)


if __name__ == '__main__':
    upload_slack('foo.txt')
