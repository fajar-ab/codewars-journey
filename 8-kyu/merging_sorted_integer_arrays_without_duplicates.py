# Rank  : 8 kyu
# Title : Merging sorted integer arrays (without duplicates)
# Link  : https://www.codewars.com/kata/573f5c61e7752709df0005d2


def merge_arrays(first, second):
    return sorted(set(first + second))
