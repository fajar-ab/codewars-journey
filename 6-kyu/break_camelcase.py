# Rank  : 6 kyu
# Title : Break camelCase
# Link  : https://www.codewars.com/kata/5208f99aee097e6552000148


def solution(s):
    upper = [c for c in s if c.isupper()]
    for x in upper: s = s.replace(x, " " + x)

    return " ".join(s.split())
