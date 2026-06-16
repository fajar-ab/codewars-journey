# Rank  : 8 kyu
# Title : Sum of Multiples
# Link  : https://www.codewars.com/kata/57241e0f440cd279b5000829


def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"

    return sum(range(n, m, n))
