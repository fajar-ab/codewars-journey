# Rank  : 7 kyu
# Title : Ones and Zeros
# Link  : https://www.codewars.com/kata/578553c3a1b8d5c40300037c

def binary_array_to_number(arr):
  bit = "".join(map(str, arr))
  return int(bit, 2)
