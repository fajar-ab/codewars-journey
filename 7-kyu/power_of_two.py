# Rank  : 7 kyu
# Title : Power of two
# Link  : https://www.codewars.com/kata/534d0a229345375d520006a0


def power_of_two(x):
    return x > 0 and (x & (x - 1)) == 0
