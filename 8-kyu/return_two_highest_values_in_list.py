# Rank  : 8 kyu
# Title : Return Two Highest Values in List
# Link  : https://www.codewars.com/kata/57ab3c09bb994429df000a4a


from heapq import nlargest


def two_highest(arg1):
    return nlargest(2, set(arg1))
