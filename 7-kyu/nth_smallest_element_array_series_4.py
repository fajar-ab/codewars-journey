# Rank  : 7 kyu
# Title : Nth Smallest Element (Array Series #4)
# Link  : https://www.codewars.com/kata/5a512f6a80eba857280000fc


def nth_smallest(arr, pos):
    return sorted(arr)[pos - 1]


print(nth_smallest([3, 1, 2], 2), 2)
