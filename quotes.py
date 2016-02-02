#!/usr/bin/env python

"""Get the current stock quotes"""

import requests


# http://stackoverflow.com/questions/27794418/free-json-formatted-stock-quote-api-live-or-historical
def quotes():
    """Get the current stock quotes"""
    url = 'http://www.google.com/finance/info?q=NSE:GOOGL,AAPL,MSFT,FB'
    response = requests.get(url)
    print response.status_code
    print response.ok


if __name__ == '__main__':
    quotes()
