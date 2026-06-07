# Rank  : 8 kyu
# Title : Testing 1-2-3
# Link  : https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9
#
def number(lines):
    return [f"{i}: {c}" for i, c in enumerate(lines, 1)]
