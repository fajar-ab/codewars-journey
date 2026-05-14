# Rank  : 7 kyu
# Title : You're a square
# Link  : https://www.codewars.com/kata/54c27a33fb7da0db0100040e

from math import sqrt

def is_square(n):
    return False if n < 0 else sqrt(n).is_integer()

print(is_square(-1))