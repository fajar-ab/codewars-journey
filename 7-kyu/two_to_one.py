# Rank  : 7 kyu
# Title : Two to One
# Link  : https://www.codewars.com/kata/reviews/5656bc4c9c771d4801000015/groups/5656c26398143b4c2f000033

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))