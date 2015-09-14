#!/usr/bin/env python

import os

def dir_size1(dir_name):
    dir_size = 0
    for curr_file in os.listdir(dir_name):
        dir_size += os.path.getsize(curr_file)
    return dir_size

def dir_size2(dir_name):
    return sum(map(os.path.getsize, os.listdir(dir_name))) 

if __name__ == '__main__':
    print dir_size1('.')
    print dir_size2('.')
