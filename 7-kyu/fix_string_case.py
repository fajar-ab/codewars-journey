# Rank  : 7 kyu
# Title : Fix string case
# Link  : https://www.codewars.com/kata/5b180e9fedaa564a7000009a


def solve(s):
    count_upper = sum(c.isupper() for c in s)
    count_lower = sum(c.islower() for c in s)

    if count_upper <= count_lower:
        return s.lower()

    return s.upper()
