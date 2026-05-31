# Rank  : 6 kyu
# Title : Find the unique number
# Link  : https://www.codewars.com/kata/585d7d5adb20cf33cb000235

def find_uniq(arr):
    (n, ) = [num for num in set(arr) if arr.count(num) == 1]
    return n   # n: unique number in the array
