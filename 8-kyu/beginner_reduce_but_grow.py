# Rank  : 8 kyu
# Title : Beginner Reduce but Grow
# Link  : https://www.codewars.com/kata/57f780909f7e8e3183000078

def grow(arr):
    multiple = 1
    for number in arr: multiple *= number

    return multiple