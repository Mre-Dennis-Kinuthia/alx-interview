#!/usr/bin/python3

def makeChange(coins, total):
    if total < 0:
        return 0
    if total == 0:
        return 0

    # Initialize a table to store the minimum number of coins needed for each total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # It takes 0 coins to make a total of 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1