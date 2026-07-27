# Rank  : 7 kyu
# Title : Difference Of Squares
# Link  : https://www.codewars.com/kata/558f9f51e85b46e9fa000025


def difference_of_squares(n):
    numbers = range(1, n + 1)
    return sum(numbers) ** 2 - sum(map(lambda x: x**2, numbers))
