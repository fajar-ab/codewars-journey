# Rank  : 7 kyu
# Title : Evens times last
# Link  : https://www.codewars.com/kata/5a1a9e5032b8b98477000004


def even_last(numbers):
    if not numbers:
        return 0

    return (
        sum(number for index, number in enumerate(numbers) if index % 2 == 0)
        * numbers[-1]
    )
