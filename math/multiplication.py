"""Multiplication

   Thus far, these will only work for the natural numbers.
"""

from utils import *

table = [
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
    [ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18],
    [ 0,  3,  6,  9, 12, 15, 18, 21, 24, 27],
    [ 0,  4,  8, 12, 16, 20, 24, 28, 32, 36],
    [ 0,  5, 10, 15, 20, 25, 30, 35, 40, 45],
    [ 0,  6, 12, 18, 24, 30, 36, 42, 48, 54],
    [ 0,  7, 14, 21, 28, 35, 42, 49, 56, 63],
    [ 0,  8, 16, 24, 32, 40, 48, 56, 64, 72],
    [ 0,  9, 18, 27, 36, 45, 54, 63, 72, 81]
]


def brute(m1, m2):
    # O(10^n)

    if m1 > m2:
        m2, m1 = m1, m2

    product = 0;
    while m1 != 0:
        product += m2
        m1 = dec(m1)

    return product

def naive(m1, m2):
    # O(n1 * n2)

    product = 0
    p1 = 0
    while m1 != 0:
        p2 = 0
        t2 = m2
        d1 = m1 % 10
        while t2 != 0:
            d2 = t2 % 10
            product += table[d1][d2] * 10**(p1 + p2)
            p2 += 1
            t2 /= 10
        p1 += 1
        m1 /= 10
    return product

def peasant(m1, m2):
    # O(log n)

    # http://en.wikipedia.org/wiki/Ancient_Egyptian_multiplication

    if m1 > m2:
        m2, m1 = m1, m2

    product = 0
    while m1 > 0:
        if m1 % 2 != 0:
            product += m2
        m1 = halve(m1)
        m2 = double(m2)
    return product

def karatsuba(m1, m2):
    pass

