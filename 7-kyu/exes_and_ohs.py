# Rank  : 7 kyu
# Title : Exes and Ohs
# Link  : https://www.codewars.com/kata/55908aad6620c066bc00002a

from collections import Counter

def xo(s):
    value = s.lower()

    if "x" not in value and "o" not in value:
        return True

    count = Counter(value)
    return count["x"] == count["o"]
