# Rank  : 7 kyu
# Title : Filter the number
# Link  : https://www.codewars.com/kata/55b051fac50a3292a9000025


def filter_string(st):
    return int("".join(c for c in st if c.isdigit()))


print(filter_string("11bb2c23c3"))
