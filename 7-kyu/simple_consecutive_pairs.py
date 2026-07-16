# Rank  : 7 kyu
# Title : Simple consecutive pairs
# Link  : https://www.codewars.com/kata/5a3e1319b6486ac96f000049


def pairs(arr):
    return sum([abs(a - b) == 1 for a, b in zip(arr[::2], arr[1::2])])


print(pairs([1, 2, 5, 8, -4, -3, 7, 6, 5]))
