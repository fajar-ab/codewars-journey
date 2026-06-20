# Rank  : 6 kyu
# Title : Highest Scoring Word
# Link  : https://www.codewars.com/kata/57eb8fcdf670e99d9b000272


def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


print(high("aa b"))
print(high("b aa"))
