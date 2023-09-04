#!/usr/bin/python3
"""
Minimum Operations Interview Question
"""


def minOperations(n):
    """
    Returns fewest number of operations needed to get exactly n characters
    """
    if n <= 1:
        return 0

    min_operations = 2
    operations = 0
    for i in range(min_operations, n + 1):
        while n % i == 0:
            n = n / i
            operations += i
    return operations
