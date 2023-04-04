from math import factorial
from collections import Counter
from fractions import gcd


def cycle_count(c, n):
    result = factorial(n)
    counts = {x: c.count(x) for x in set(c)}
    for i, j in counts.items():
        result //= (i**j) * factorial(j)
    return result


def permutations(n, i=1):
    if n == 0:
        return [[]]
    result = []
    for j in range(i, n + 1):
        for p in permutations(n - j, j):
            result.append([j] + p)
    return result


def solution(w, h, s):
    grid = 0
    for row in permutations(w):
        for column in permutations(h):
            total_gcd = 0
            for j in column:
                row_gcd = 0
                for i in row:
                    row_gcd += gcd(i, j)
                total_gcd += row_gcd
            m = cycle_count(row, w) * cycle_count(column, h)
            grid += m * (s**total_gcd)
    return str(grid // (factorial(w) * factorial(h)))
