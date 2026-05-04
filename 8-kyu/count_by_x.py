# Rank  : 8 kyu
# Title : Count by X
# Link  : https://www.codewars.com/kata/5513795bd3fafb56c200049e

def count_by(x, n):
    return list(range(x, n * x + 1, x))
