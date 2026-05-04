# Rank  : 7 kyu
# Title : Descending Order
# Link  : https://www.codewars.com/kata/reviews/5467e4de2edf8bbf40000157/groups/69f81dd54f11ffd61b8ec42c

def descending_order(num):
    s = sorted(str(num), reverse=True)
    return int("".join(s))
