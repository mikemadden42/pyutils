#!/usr/bin/env python

# http://pymotw.com/2/multiprocessing/basics.html

import multiprocessing
import os
import urllib2


def get(url):
    try:
        f = urllib2.urlopen(url)
        # if f.msg == 'OK':
        #     print 'url:', f.url
        #     print 'code:', f.code
        #     print 'message:', f.msg
        #     data = f.read()
        #     print 'bytes read:', len(data)
        #     print
    except Exception as e:
        print(url)
        print(e)


def check():
    with open('urls.txt', 'r') as file:
        jobs = []
        for url in file:
            url = url.rstrip(os.linesep)
            p = multiprocessing.Process(target=get, args=(url,))
            jobs.append(p)
            p.start()


if __name__ == '__main__':
    check()
