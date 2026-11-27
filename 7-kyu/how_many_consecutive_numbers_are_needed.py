# Rank  : 7 kyu
# Title : How many consecutive numbers are needed?
# Link  : https://www.codewars.com/kata/559cc2d2b802a5c94700000c


def consecutive(arr):
    if len(arr) < 2:
        return 0

    arr.sort()

    first, last = arr[0], arr[-1]
    step = 1 if first <= last else -1

    return len([i for i in range(first, last, step) if i not in arr])
