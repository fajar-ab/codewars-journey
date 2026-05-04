# Rank  : 6 kyu
# Title : Persistent Bugger
# Link  : https://www.codewars.com/kata/reviews/55c7dba2ea4fa879c4000015/groups/69f83793a5c2031f35678543

from math import prod

def persistence(n, counter=0):
    """gunkan recursion untuk setiap multiplications dan hitung 
    setiap recursion sampai n 0-9 dan kembalikan nilai iteraksinya"""

    if n in range(10):
        return counter

    return persistence(prod(map(int, str(n))), counter + 1)

