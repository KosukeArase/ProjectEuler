# https://projecteuler.net/problem=4


import math
import itertools

from problem3 import get_factors


def get_largest_palindromic(N):
    maximum, minimum = 10**N - 1, 10**(N - 1)
    ranges = [range(9, 0, -1)] + [range(9, -1, -1)] * (N-1)

    for digits in itertools.product(*ranges):
        palindromic = sum([digits[i] * (10**(N*2-i-1) + 10**i) for i in range(N)])
        factors_dict = get_factors(palindromic) # {p_1: c_1, p_2: c_2, ...} for p_1^c_1 * p_2^c_2 * ...

        factors = list(factors_dict.keys())
        factors.sort()

        if factors_dict[factors[-1]] > maximum:
            continue

        nums = [1, 1]
        is_valid = True

        for p in factors[::-1]:
            c = factors_dict[p]
            for i in range(c):
                larger = 0 if nums[0] > nums[1] else 1
                smaller = (larger + 1) % 2
                if nums[larger] * p <= maximum:
                    nums[larger] *= p
                elif nums[smaller] * p <= maximum:
                    nums[smaller] *= p
                else:
                    is_valid = False
                    break

            if not is_valid:
                break

        if is_valid and ((minimum <= min(nums)) and (max(nums) <= maximum)):
            return palindromic, nums


if __name__ == '__main__':
    N = int(input('Get the largest palindromic number made from the product of two N-digit numbers, input N: '))
    palindromic, [m, n] = get_largest_palindromic(N)

    print('{} = {} x {}'.format(palindromic, m, n))

