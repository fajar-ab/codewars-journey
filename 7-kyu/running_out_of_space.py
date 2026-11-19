# Rank  : 7 kyu
# Title : Running out of space
# Link  : https://www.codewars.com/kata/56576f82ab83ee8268000059


def spacey(array):
    return ["".join(array[:i]) for i in range(1, len(array) + 1)]
