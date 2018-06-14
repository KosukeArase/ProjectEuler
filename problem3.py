# https://projecteuler.net/problem=3


import math
from collections import defaultdict


def devide(n, i, factors):
    while n % i == 0:
        factors[i] += 1
        n /= i
    return n


def get_factors(n):
    i, primes, factors = 3, [2], defaultdict(int)
    n = devide(n, 2, factors)

    while True:
        is_prime = True
        for p in primes:
            if p > int(math.sqrt(i)): # any p cannot devide i
                break
            elif i % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)
            n = devide(n, i, factors)

        if i > int(math.sqrt(n)):
            if n != 1: #prime
                primes.append(int(n))
                factors[int(n)] = 1
            break

        i += 2

    return factors


if __name__ == '__main__':
    N = int(input())
    factors = get_factors(N)

    print(max(list(factors.keys())))

