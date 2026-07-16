# Rank  : 7 kyu
# Title : Smallest value of an array
# Link  : https://www.codewars.com/kata/544a54fd18b8e06d240005c0


def find_smallest(numbers, to_return):
    return {"value": min(numbers), "index": numbers.index(min(numbers))}.get(to_return)
