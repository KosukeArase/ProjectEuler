# https://projecteuler.net/problem=3


import math
from collections import defaultdict

def get_factors(n):
    i = 3
    primes = [2]
    factors = defaultdict(int)

    while True:
        is_prime = True
        for p in primes:
            if p > int(math.sqrt(i)): # nothing in p can devide i
                break
            elif i % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

        while n % i == 0:
            factors[i] += 1
            n /= i

        if i > int(math.sqrt(n)):
            if n != 1:
                primes.append(int(n))
                factors[int(n)] = 1
            break
        i += 1

    return factors


def main():
    N = int(input())
    factors = get_factors(N)

    print(max(list(factors.keys())))


if __name__ == '__main__':
    main()