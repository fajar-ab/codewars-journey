# Rank  : 8 kyu
# Title : Find the first non-consecutive number
# Link  : https://www.codewars.com/kata/58f8a3a27a5c28d92e000144


def first_non_consecutive(arr):
    for i in range(len(arr) - 1):
        if arr[i] + 1 != (n := arr[i + 1]):
            return n

    return None


print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]))
