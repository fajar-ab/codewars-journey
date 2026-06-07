# Rank  : 7 kyu
# Title : RaNDoM CAsE
# Link  : https://www.codewars.com/kata/57073869924f34185100036d

from random import choice


def random_case(x):
    return "".join(choice([c.lower(), c.upper()]) for c in x)
