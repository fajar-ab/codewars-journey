# Rank  : 7 kyu
# Title : Compare Strings by Sum of Chars
# Link  : https://www.codewars.com/kata/576bb3c4b1abc497ec000065


def compare(s1, s2):
    s1 = map(ord, s1.upper()) if s1 and s1.isalpha() else []
    s2 = map(ord, s2.upper()) if s2 and s2.isalpha() else []

    return sum(s1) == sum(s2)


print(compare(None, ""))
