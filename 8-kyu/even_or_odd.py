# Rank  : 8 kyu
# Title : Even or Odd
# Link  : https://www.codewars.com/kata/53da3dbb4a5168369a0000fe

def even_or_odd(number):
    return ["Even", "Odd"][number & 1]
