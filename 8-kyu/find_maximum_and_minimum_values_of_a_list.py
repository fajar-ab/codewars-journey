# Rank  : 8 kyu
# Title : Find Maximum and Minimum Values of a List
# Link  : https://www.codewars.com/kata/577a98a6ae28071780000989

def minimum(arr):
    number = float('inf')
    for value in arr:
        if value < number:
            number = value
    return number

def maximum(arr):
    number = float('-inf')
    for value in arr:
        if value > number:
            number = value
    return number