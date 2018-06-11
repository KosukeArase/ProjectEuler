# https://projecteuler.net/problem=4

import math
import itertools

from problem3 import get_factors

"""
2: 10~99 -> 100~9801
3: 100~999 -> 10000~998001
"""


def get_largest_palindromic(N):
    ranges = [range(9, 0, -1)] + [range(9, -1, -1)] * (N-1)
    for digits in itertools.product(*ranges): # 999, 998, ..., 100
        palindromic = sum([digits[i] * (10**(N*2-i-1) + 10**i) for i in range(N)])
        factors = get_factors(palindromic) # [p_1, c_1], [[p_2, c_2], ...] for p_1^c_1 * p_2^c_2 * ...

        if factors[-1][0] >= 10**N:
            continue

        m, n = 1, 1
        is_valid = True

        for p, c in factors[::-1]:
            for i in range(c):
                if m < n:
                    if n * p < 10**N:
                        n *= p
                    else:
                        m *= p
                    if m >= 10**N:
                        is_valid = False
                        break
                else: # m > n:
                    if m * p < 10**N:
                        m *= p
                    else:
                        n *= p
                    if n >= 10**N:
                        is_valid = False
                        break
            if not is_valid:
                break

        if not ((10**(N-1) <= m < 10**N) and (10**(N-1) <= n < 10**N)):
            is_valid = False

        if is_valid:
            return palindromic, m, n


def main():
    """
    
    """ 
    N = int(input('Get the largest palindromic number made from the product of two N-digit numbers, input N: '))

    palindromic, m, n = get_largest_palindromic(N)

    print('{} is the largest palindromic number made from the product of two 3-digit numbers ({} x {})'.format(palindromic, m, n))



if __name__ == '__main__':
    main()