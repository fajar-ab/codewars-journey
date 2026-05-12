# Rank  : 8 kyu
# Title : Count of positives / sum of negatives
# Link  : https://www.codewars.com/kata/576bb71bbbcf0951d5000044

def count_positives_sum_negatives(arr):
    return [
        sum(1 for n in arr if n > 0),
        sum(n for n in arr if n < 0)
    ] if arr else []
