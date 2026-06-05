# Rank  : 8 kyu
# Title : Grasshopper - Summation
# Link  : https://www.codewars.com/kata/55d24f55d7dd296eb9000030


def summation(num):
    return sum(i for i in range(1, num + 1))


assert summation(1) == 1
assert summation(8) == 36
assert summation(22) == 253
assert summation(100) == 5050
