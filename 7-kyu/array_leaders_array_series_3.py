# Rank  : 7 kyu
# Title : Array Leaders (Array Series #3)
# Link  : https://www.codewars.com/kata/5a651865fd56cb55760000e0


def array_leaders(numbers):
    return [n for i, n in enumerate(numbers, 1) if n > sum(numbers[i:])]
