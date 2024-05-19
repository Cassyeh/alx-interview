#!/usr/bin/python3
"""
Module for prime game function
"""


def sieve(n):
    """
    function generates all prime numbers up to a given number n
    """
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes

def isWinner(x, nums):
    """
    determines the winner using the game_winner function
    returns the player with the most wins or None if there's a tie
    """
    if x == 0 or not nums:
        return None

    max_num = max(nums)
    primes = sieve(max_num)

    def game_winner(n):
        """
        uses a boolean list to mark numbers as available or removed: sieve_list
        """
        if n < 2:
            return 'Ben'
        moves = 0
        sieve_list = [True] * (n + 1)
        for prime in primes:
            if prime > n:
                break
            if sieve_list[prime]:
                moves += 1
                for multiple in range(prime, n + 1, prime):
                    sieve_list[multiple] = False
        return 'Maria' if moves % 2 != 0 else 'Ben'

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if game_winner(n) == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
