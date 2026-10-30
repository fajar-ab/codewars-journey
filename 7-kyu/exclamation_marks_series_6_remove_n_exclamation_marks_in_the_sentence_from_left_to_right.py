# Rank  : 7 kyu
# Title : Exclamation marks series #6: Remove n exclamation marks in the sentence from left to right
# Link  : https://www.codewars.com/kata/57faf7275c991027af000679

import re


def remove(st, n):
    return re.sub(r"!", "", st, count=n)
