#!/usr/bin/python3
""" Prime Number game """


def isWinner(x, nums):
    """ returns the winner of the game
    where x is the number of rounds and
    nums is an array of n values
    """
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes = sieve(max_num)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1
            continue

        prime_count = sum(primes[2:n+1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def sieve(n):
    """ seives out prime numbers in n """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for start in range(2, int(n**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start*start, n + 1, start):
                is_prime[multiple] = False
    return is_prime
