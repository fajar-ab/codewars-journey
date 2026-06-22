# Rank  : 7 kyu
# Title : Love vs friendship
# Link  : https://www.codewars.com/kata/59706036f6e5d1e22d000016


def words_to_marks(s):
    return sum(map(lambda c: ord(c) - 96, s))
