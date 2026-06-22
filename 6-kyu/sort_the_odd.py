# Rank  : 6 kyu
# Title : Sort the odd
# Link  : https://www.codewars.com/kata/578aa45ee9fd15ff4600090d


def sort_array(source_array):
    odd_numbers = iter(sorted(num for num in source_array if num % 2))
    return [next(odd_numbers) if num % 2 else num for num in source_array]
