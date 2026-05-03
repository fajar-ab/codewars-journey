# Rank  : 8 kyu
# Title : Find the smallest integer in the array
# Link  : https://www.codewars.com/kata/55a2d7ebe362935a210000b2

def find_smallest_int(arr):
    small_number = float('inf')
    for number in arr:
        if number < small_number: small_number = number

    return small_number

print(find_smallest_int([78, 56, 232, 12, 11, -43]))