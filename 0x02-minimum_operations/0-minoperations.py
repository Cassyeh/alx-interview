#!/usr/bin/python3
"""
Minimum Operations Module
"""


def minOperations(n):
    """
    method that calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    Given a number n
    """
    now = 1
    head = 0
    counter = 0
    while now < n:
        remainder = n - now
        if (remainder % now == 0):
            head = now
            now += head
            counter += 2
        else:
            now += head
            counter += 1
    return counter
