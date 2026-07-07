# Rank  : 7 kyu
# Title : Sort by Last Char
# Link  : https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0


def last(s):
    return list(sorted(s.split(), key=lambda x: x[-1]))
