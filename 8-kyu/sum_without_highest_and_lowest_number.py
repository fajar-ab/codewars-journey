# Rank  : 8 kyu
# Title : Sum without highest and lowest number
# Link  : https://www.codewars.com/kata/576b93db1129fcf2200001e6

def sum_array(arr):
    if not arr or len(arr) < 2: return 0
    return sum(sorted(arr)[1:-1])

print(sum_array([]))
