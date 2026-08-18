# Rank  : 8 kyu
# Title : Find the Integral
# Link  : https://www.codewars.com/kata/59811fd8a070625d4c000013


def integrate(coefficient, exponent):
    exponent += 1
    coefficient //= exponent
    return f"{coefficient}x^{exponent}"
