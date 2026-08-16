# Rank  : 7 kyu
# Title : Basic Sequence Practice
# Link  : https://www.codewars.com/kata/5436f26c4e3d6c40e5000282


def sum_of_n(n):
    step = 1 if n >= 0 else -1
    return [int(step * (i * (i + 1)) / 2) for i in range(abs(n) + 1)]
