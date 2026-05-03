# Rank  : 7 kyu
# Title : Sum of odd numbers
# Link  : https://www.codewars.com/kata/reviews/55fd79555342550aa3000009/groups/55fd931e4a50971295000035

"""
n1  1                      = 1   = 1 ** 3
n2  3 + 5                  = 8   = 2 ** 3
n3  7 + 9 + 11             = 27  = 3 ** 3
n4  13 + 15 + 17 + 19      = 64  = 4 ** 3
n5  21 + 23 + 25 + 27 + 29 = 125 = 5 ** 3 
"""
def row_sum_odd_numbers(n):
    return n ** 3
