# Rank  : 8 kyu
# Title : Find the stray number
# Link  : https://www.codewars.com/kata/57f609022f4d534f05000024

def stray(arr):
    """menggunakan min untuk membandingkan, dan
    menentukan “mana yang paling kecil”"""
    return min(arr, key=arr.count)

print(stray([1, 1, 1, 1, 1, 1, 2]))

