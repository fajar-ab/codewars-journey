# Rank  : 6 kyu
# Title : Consonant value
# Link  : https://www.codewars.com/kata/59c633e7dcc4053512000073

from re import split


def solve(s):
    return max(sum(ord(c) - 96 for c in sub) for sub in split(r"[aiueo]", s) if sub)
