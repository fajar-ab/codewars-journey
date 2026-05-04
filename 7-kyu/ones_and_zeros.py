# Rank  : 7 kyu
# Title : Ones and Zeros
# Link  : https://www.codewars.com/kata/reviews/578670e7d9456ea80500005e/groups/69f8435aa5c2031f3567868a

def binary_array_to_number(arr):
  bit = "".join(map(str, arr))
  return int(bit, 2)
