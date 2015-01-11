#!/usr/bin/env python3.4

# http://stackoverflow.com/questions/1006289/how-to-find-out-the-number-of-cpus-using-python

import multiprocessing

def cpus():
    print('CPUs: %d' % (multiprocessing.cpu_count()))

if __name__ == '__main__':
    cpus()
