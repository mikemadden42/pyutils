#!/usr/bin/env python
"""Get the current stock quotes"""

import requests
import six


# http://stackoverflow.com/questions/27794418/free-json-formatted-stock-quote-api-live-or-historical
def quotes():
    """Get the current stock quotes"""
    url = 'http://www.google.com/finance/info?q=NSE:GOOGL,AAPL,MSFT,FB'
    response = requests.get(url)
    six.print_(response.status_code)
    six.print_(response.ok)


if __name__ == '__main__':
    quotes()
