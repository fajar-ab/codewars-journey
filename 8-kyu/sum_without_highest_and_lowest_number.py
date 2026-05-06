# Rank  : 8 kyu
# Title : Sum without highest and lowest number
# Link  : https://www.codewars.com/kata/reviews/578dc610f50c0d6764000025/groups/57c019764f5f01b5db000023

def sum_array(arr):
    if not arr or len(arr) < 2: return 0
    return sum(sorted(arr)[1:-1])

print(sum_array([]))
