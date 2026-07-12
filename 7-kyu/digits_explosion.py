# Rank  : 7 kyu
# Title : Digits explosion
# Link  : https://www.codewars.com/kata/585b1fafe08bae9988000314


def explode(s):
    return "".join(num * int(num) for num in s)
