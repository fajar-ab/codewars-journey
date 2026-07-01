# Rank  : 7 kyu
# Title : Find twins
# Link  : https://www.codewars.com/kata/5834315e06f227a6ac000099


from collections import Counter


def elimination(arr):
    counts = Counter(arr)
    for n, c in counts.items():
        if c > 1:
            return n

    return None
