# Rank  : 8 kyu
# Title : Name on billboard
# Link  : https://www.codewars.com/kata/570e8ec4127ad143660001fd


from math import prod


def billboard(name, price=30):
    return prod({len(name), price})
