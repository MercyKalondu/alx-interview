#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n)
    '''
    write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file
    '''
    result = 0
    index = 2
    if n < 2:
        return 0

    while (index < n + 1):
        while n % index == 0:
            result += index
            n /= index
        index += 1
        return result
