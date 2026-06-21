# Rank  : 7 kyu
# Title : Candy problem
# Link  : https://www.codewars.com/kata/55466644b5d240d1d70000ba


def candies(lst):
    return -1 if len(lst) <= 1 else sum(max(lst) - n for n in lst)


print(candies([5, 8, 6, 4]))
