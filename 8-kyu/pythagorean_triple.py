# Rank  : 8 kyu
# Title : Pythagorean Triple
# Link  : https://www.codewars.com/kata/5951d30ce99cf2467e000013


def pythagorean_triple(integers):
    a, b, c = sorted(integers)
    return (a * a + b * b) == c * c
