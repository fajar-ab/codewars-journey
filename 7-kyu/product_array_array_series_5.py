# Rank  : 7 kyu
# Title : Product Array (Array Series #5)
# Link  : https://www.codewars.com/kata/5a905c2157c562994900009d


def product_array(numbers):
    total = 1
    for n in numbers:
        total *= n
    return [total // n for n in numbers]
