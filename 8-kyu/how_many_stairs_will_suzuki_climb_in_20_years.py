# Rank  : 8 kyu
# Title : How many stairs will Suzuki climb in 20 years?
# Link  : https://www.codewars.com/kata/56fc55cd1f5a93d68a001d4e


from itertools import chain


def stairs_in_20(stairs):
    return sum(chain.from_iterable(stairs)) * 20
