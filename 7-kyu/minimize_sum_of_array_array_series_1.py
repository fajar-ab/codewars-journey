# Rank  : 7 kyu
# Title : Minimize Sum Of Array (Array Series #1)
# Link  : https://www.codewars.com/kata/5a523566b3bfa84c2e00010b


def min_sum(arr):
    arr.sort()
    return sum(arr[i] * arr[~i] for i in range(len(arr) // 2))
