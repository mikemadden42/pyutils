#!/usr/bin/env python3
"""Test the import of secondary python libraries"""

import sys

try:
    import boto
    import boto3
    import dateutil
    import jinja2
    import nose
    import psutil
    import pytest
    import requests
    import six
    import slacker
    import yaml
except ModuleNotFoundError as ex:
    print(ex)
    sys.exit(1)


def test_imports():
    """Test the import of secondary python libraries"""
    six.print_("boto3: %s" % (boto3.__version__))
    six.print_("boto: %s" % (boto.__version__))
    six.print_("dateutil: %s" % (dateutil.__version__))
    six.print_("jinja2: %s" % (jinja2.__version__))
    six.print_("nose: %s" % (nose.__version__))
    six.print_("psutil: %s" % (psutil.__version__))
    six.print_("pytest: %s" % (pytest.__version__))
    six.print_("requests: %s" % (requests.__version__))
    six.print_("six: %s" % (six.__version__))
    six.print_("slacker: %s" % (slacker.__version__))
    six.print_("yaml: %s" % (yaml.__version__))


if __name__ == "__main__":
    test_imports()
