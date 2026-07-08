# Rank  : 7 kyu
# Title : Currying functions: multiply all elements in an array
# Link  : https://www.codewars.com/kata/586909e4c66d18dd1800009b


def multiply_all(arr):
    return lambda multiplier: [x * multiplier for x in arr]
