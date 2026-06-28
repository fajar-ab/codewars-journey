# Rank  : 6 kyu
# Title : Array.diff
# Link  : https://www.codewars.com/kata/523f5d21c841566fde000009


def array_diff(a, b):
    return [x for x in a if x not in b]


a = [1, 2]
b = [1]
print(a, b, "=", array_diff(a, b))

a = [1, 2, 2, 2, 3]
b = [2]
print(a, b, "=", array_diff(a, b))
