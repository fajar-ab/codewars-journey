# Rank  : 8 kyu
# Title : Find the smallest integer in the array
# Link  : https://www.codewars.com/kata/reviews/55f2a5340fd3077553000031/groups/69f71b1ffd3b596b175b0b54

def find_smallest_int(arr):
    small_number = float('inf')
    for number in arr:
        if number < small_number: small_number = number

    return small_number

print(find_smallest_int([78, 56, 232, 12, 11, -43]))