# Rank  : 8 kyu
# Title : Beginner Reduce but Grow
# Link  : https://www.codewars.com/kata/reviews/5806763a0be9a293e40000da/groups/628cf8b2a10ab10001bdafda

def grow(arr):
    multiple = 1
    for number in arr: multiple *= number

    return multiple