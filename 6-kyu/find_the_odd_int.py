# Rank  : 6 kyu
# Title : Find the odd int
# Link  : https://www.codewars.com/kata/54da5a58ea159efa38000836


from collections import Counter


def find_it(seq):
    return [i for i, v in Counter(seq).items() if v % 2 != 0][0]
