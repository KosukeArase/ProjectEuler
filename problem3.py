# https://projecteuler.net/problem=3

import math


def get_factors(n):
    i = 3
    primes = [2]
    factors = []

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

        if n % i == 0:
            factors.append([i, 0])
        while n % i == 0:
            n /= i
            factors[-1][1] += 1

        if i > int(math.sqrt(n)):
            if n != 1:
                primes.append(int(n))
                factors.append([int(n), 1])
            break
        i += 1

    return factors


def main():
    N = int(input())
    factors = get_factors(N)

    print(factors[-1][0])


if __name__ == '__main__':
    main()