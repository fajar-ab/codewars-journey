# Rank  : 7 kyu
# Title : Find the next perfect square
# Link  : https://www.codewars.com/kata/56269eb78ad2e4ced1000013

from math import isqrt

def find_next_square(sq):
    if (root := isqrt(sq)) ** 2 == sq:
        return (root + 1) ** 2

    return -1
