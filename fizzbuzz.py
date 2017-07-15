#!/usr/bin/env python
"""
Prints the integers from 1 to 100 (inclusive).

But:
for multiples of three, print Fizz (instead of the number)
for multiples of five, print Buzz (instead of the number)
for multiples of both three and five,  print FizzBuzz (instead of the number)
"""

import six
from six.moves import range


def fizzbuzz():
    """Prints the integers from 1 to 100 (inclusive)."""
    for i in range(1, 101):
        if i % 15 == 0:
            six.print_('FizzBuzz')
        elif i % 3 == 0:
            six.print_('Fizz')
        elif i % 5 == 0:
            six.print_('Buzz')
        else:
            six.print_(i)


if __name__ == '__main__':
    fizzbuzz()
