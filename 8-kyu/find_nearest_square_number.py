# Rank  : 8 kyu
# Title : Find Nearest square number
# Link  : https://www.codewars.com/kata/5a805d8cafa10f8b930005ba

from math import sqrt


def nearest_sq(n):
    return round(sqrt(n)) ** 2
