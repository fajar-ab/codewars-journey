# Rank  : 7 kyu
# Title : Find all occurrences of an element in an array
# Link  : https://www.codewars.com/kata/59a9919107157a45220000e1


def find_all(array, n):
    return [index for index, number in enumerate(array) if number == n]
