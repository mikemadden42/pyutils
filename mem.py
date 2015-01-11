#!/usr/bin/env python3.4

# http://stackoverflow.com/questions/22102999/get-total-physical-memory-from-python

from psutil import virtual_memory

def memory():
    mem = virtual_memory()
    print(mem.total)

if __name__ == '__main__':
    memory()
