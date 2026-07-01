# Rank  : 7 kyu
# Title : max diff - easy
# Link  : https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095


def max_diff(list):
    return max(list) - min(list) if list else 0
