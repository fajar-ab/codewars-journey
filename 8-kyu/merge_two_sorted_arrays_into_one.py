# Rank  : 8 kyu
# Title : Merge two sorted arrays into one
# Link  : https://www.codewars.com/kata/5899642f6e1b25935d000161


def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))
