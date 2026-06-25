# Rank  : 7 kyu
# Title : Simetri alfabet
# Link  : https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0


def solve(strings: list[str]):
    alphabet = "_abcdefghijklmnopqrstuvwxyz"

    return [
        sum(i == alphabet.index(c) for i, c in enumerate(char, 1))
        for char in map(str.lower, strings)
    ]


print(solve(["abode", "ABc", "xyzD"]))
