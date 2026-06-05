# Rank  : 8 kyu
# Title : No zeros for heroes
# Link  : https://www.codewars.com/kata/570a6a46455d08ff8d001002


def no_boring_zeros(n):
    return n and int(str(n).rstrip("0"))
