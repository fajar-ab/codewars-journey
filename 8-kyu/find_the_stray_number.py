# Rank  : 8 kyu
# Title : Find the stray number
# Link  : https://www.codewars.com/kata/57f609022f4d534f05000024

def stray(arr):
    """pastikan hanya ada satu value yang unik di list
    jika lebih xor tidak akan berkerja mencari value unik"""
    result = 0
    for value in arr:
        result ^= value
    return result

print(stray([1, 1, 1, 1, 1, 1, 2]))

