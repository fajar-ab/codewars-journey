# Rank  : 7 kyu
# Title : Most digits
# Link  : https://www.codewars.com/kata/58daa7617332e59593000006


def find_longest(arr):
    return max(map(str, arr), key=len)
