# Rank  : 7 kyu
# Title : Simple remove duplicates
# Link  : https://www.codewars.com/kata/5ba38ba180824a86850000f7


def solve(arr):
    x = list(dict.fromkeys(arr))
    return x if x[0] != arr[-1] else x[1:] + [arr[-1]]


print(solve([3, 4, 4, 3, 6, 3]))
