#!/usr/bin/python3
"""
Prime Game Interview Question
"""


def findPrimes(n):
    """
    Returns list of primes upto n using the sieve of Eratosthenes algorithm
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(pow(n, 0.5)) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False

    primes = [i for i in range(2, n + 1) if sieve[i]]
    return primes


def isWinner(x, nums):
    """
    Solution for prime game
    """
    if x <= 0 or not nums:
        return None

    # Player1 = Maria
    # Player2 = Ben
    player1 = player2 = 0
    for i in range(x):
        if nums[i] == 0:
            continue
        counter = len(findPrimes(nums[i]))
        if (counter % 2) == 0:
            player2 += 1
        else:
            player1 += 1

    if player1 > player2:
        return 'Maria'
    elif player2 > player1:
        return 'Ben'
    return None
