#!/usr/bin/env python

"""Get the status of a set of urls."""

# http://chriskiehl.com/article/parallelism-in-one-line
# https://docs.python.org/2/library/multiprocessing.html
# http://stackoverflow.com/questions/26432411/multiprocessing-dummy-in-python
# http://stackoverflow.com/questions/4319236/remove-the-newline-character-in-a-list-read-from-a-file
# http://sebastianraschka.com/Articles/2014_multiprocessing_intro.html
# http://www.phpied.com/downloading-top-x-sites-data-with-zombiejs/
# https://support.alexa.com/hc/en-us/articles/200449834-Does-Alexa-have-a-list-of-its-top-ranked-websites

# Find the number of threads for a python process:
# ps -o nlwp $(pgrep python)

import requests
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import cpu_count


def get(url):
    """Get the status of a given url."""
    try:
        return requests.get(url)
    except Exception as error:
        print(url, error)


def check():
    """Get the status of a set of urls."""
    infile = open('urls.txt', 'r')
    urls = [x.strip() for x in infile.readlines()]

    pool = ThreadPool(cpu_count() * 4)
    results = pool.map(get, urls)

    for result in results:
        if result is not None:
            if result.status_code != requests.codes.ok:
                print('Invalid status code', result.url)
            if len(result.content) == 0:
                print('Invalid content length', result.url)

    pool.close()
    pool.join()


if __name__ == '__main__':
    check()
