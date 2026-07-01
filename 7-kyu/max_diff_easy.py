# Rank  : 7 kyu
# Title : max diff - easy
# Link  : https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095


def max_diff(lst):
    if len(lst) > 1:
        a, *_, b = sorted(lst)
        return b - a

    return 0
