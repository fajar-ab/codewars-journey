# Rank  : 8 kyu
# Title : Enumerable Magic #1 - True for All?
# Link  : https://www.codewars.com/kata/54598d1fcbae2ae05200112c


def _all(seq, fun):
    return all(map(fun, seq))
