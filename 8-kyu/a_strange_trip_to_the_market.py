# Rank  : 8 kyu
# Title : A Strange Trip to the Market
# Link  : https://www.codewars.com/kata/55ccdf1512938ce3ac000056


import re


def is_loch_ness_monster(string):
    return bool(re.search(r"tree fiddy|three fifty|3\.50", string))
