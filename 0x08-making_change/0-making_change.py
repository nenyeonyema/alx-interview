#!/usr/bin/python3
""" Make change with a coin """


def makeChange(coins, total):
    """
    Returns the fewest number of
    coins needed to meet total
    """

    if total <= 0:
        return 0
    
    # Initialize dp array with infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case
    
    # Update dp for each coin
    for coin in coins:
        for x in range(coin, total + 1):
            if dp[x - coin] != float('inf'):
                dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
