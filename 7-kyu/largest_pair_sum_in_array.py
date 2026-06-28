# Rank  : 7 kyu
# Title : Largest pair sum in array
# Link  : https://www.codewars.com/kata/556196a6091a7e7f58000018


from heapq import nlargest


def largest_pair_sum(numbers):
    return sum(nlargest(2, numbers))
