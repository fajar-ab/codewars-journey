# Rank  : 7 kyu
# Title : esreveR
# Link  : https://www.codewars.com/kata/5413759479ba273f8100003d


def reverse(lst):
    result = list()
    for item in lst:
        result.insert(0, item)
    return result
