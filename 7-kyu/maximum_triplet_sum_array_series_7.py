# Rank  : 7 kyu
# Title : Maximum Triplet Sum (Array Series #7)
# Link  : https://www.codewars.com/kata/5aa1bcda373c2eb596000112

from heapq import nlargest


def max_tri_sum(numbers):
    return sum(nlargest(3, set(numbers)))
