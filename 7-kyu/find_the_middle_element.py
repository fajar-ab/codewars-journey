# Rank  : 7 kyu
# Title : Find the middle element
# Link  : https://www.codewars.com/kata/545a4c5a61aa4c6916000755


def gimme(input_array):
    middle = sorted(input_array)[len(input_array) // 2]
    return input_array.index(middle)


print(gimme([2, 3, 1]))
