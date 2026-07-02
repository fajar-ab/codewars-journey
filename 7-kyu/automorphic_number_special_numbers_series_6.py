# Rank  : 7 kyu
# Title : Automorphic Number (Special Numbers Series #6)
# Link  : https://www.codewars.com/kata/5a58d889880385c2f40000aa


def automorphic(n):
    return ("Not!!", "Automorphic")[str(n**2).endswith(str(n))]
