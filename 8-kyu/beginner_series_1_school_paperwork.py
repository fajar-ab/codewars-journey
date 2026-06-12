# Rank  : 8 kyu
# Title : Beginner Series #1 School Paperwork
# Link  : https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd


def paperwork(n, m):
    return max(0, n) * max(0, m)


assert paperwork(5, 5) == 25
assert paperwork(1, 2) == 2
assert paperwork(-5, 5) == 0
assert paperwork(5, -5) == 0
assert paperwork(-5, -5) == 0
assert paperwork(5, 0) == 0
