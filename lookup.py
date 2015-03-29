#!/usr/bin/env python

import os
import socket
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import cpu_count


def find(host):
    try:
        ip = socket.gethostbyname(host)
        return(host, ip)
    except socket.error as msg:
        print(host, msg)


def lookup():
    f = open('hosts.txt', 'r')
    urls = [x.strip() for x in f.readlines()]

    pool = ThreadPool(cpu_count() * 4)
    results = pool.map(find, urls)

    for r in results:
        if r is not None:
            print(r)

    pool.close()
    pool.join()

if __name__ == '__main__':
    lookup()
