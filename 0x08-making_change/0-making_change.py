#!/usr/bin/python3
"""
Function for makeChange declared
"""


def makeChange(coins, total):
    """
    Function to take a list of coins and then calculate
    how much change the total will require
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
