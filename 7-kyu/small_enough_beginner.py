# Rank  : 7 kyu
# Title : Small enough Beginner
# Link  : https://www.codewars.com/kata/57cc981a58da9e302a000214


def small_enough(array, limit):
    return all(number <= limit for number in array)
