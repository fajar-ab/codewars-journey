# Rank  : 7 kyu
# Title : Friends
# Link  : https://www.codewars.com/kata/5ad29cd95e8240dd85000b54


import math


def friends(n):
    if n <= 0:
        return 0
    total_people = math.ceil(math.log2(n))
    return max(0, total_people - 1)
