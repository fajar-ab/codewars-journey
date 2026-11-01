# Rank  : 7 kyu
# Title : Unique string characters
# Link  : https://www.codewars.com/kata/5a262cfb8f27f217f700000b


def solve(a, b):
    return "".join(c for c in a if c not in b) + "".join(c for c in b if c not in a)
