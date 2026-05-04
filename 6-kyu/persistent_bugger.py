# Rank  : 6 kyu
# Title : Persistent Bugger
# Link  : https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

from math import prod

def persistence(n, counter=0):
    """gunkan recursion untuk setiap multiplications dan hitung 
    setiap recursion sampai n 0-9 dan kembalikan nilai iteraksinya"""

    if n in range(10):
        return counter

    return persistence(prod(map(int, str(n))), counter + 1)

