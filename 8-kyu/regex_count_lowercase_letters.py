# Rank  : 8 kyu
# Title : Regex count lowercase letters
# Link  : https://www.codewars.com/kata/56a946cd7bd95ccab2000055

import re


def lowercase_count(strng):
    return len(re.findall(r"[a-z]", strng))
