# Rank  : 8 kyu
# Title : Find Maximum and Minimum Values of a List
# Link  : https://www.codewars.com/kata/reviews/5782a87d302147c020000037/groups/69fb2ef72a35f79c75870971

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