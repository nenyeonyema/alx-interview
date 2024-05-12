#!/usr/bin/python3
""" Minumum Operations """


def minOperations(n):
    """
    Calculate the fewest number of operations
    needed to result in exactly n H characters
    """
    if n <= 1:
        return 0
    
    dp = [float('inf')] * (n + 1)  # Initialize a dynamic programming array
    
    # Base cases
    dp[1] = 0  # To achieve one 'H' character, no operations are needed
    
    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    
    return dp[n]
