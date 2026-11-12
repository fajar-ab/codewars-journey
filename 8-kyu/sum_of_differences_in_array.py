# Rank  : 8 kyu
# Title : Sum of differences in array
# Link  : https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e


from itertools import pairwise


def sum_of_differences(arr):
    return sum(a - b for a, b in pairwise(sorted(arr, reverse=True)))
