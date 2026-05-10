# Rank  : 7 kyu
# Title : Sum Array with different bases
# Link  : https://www.codewars.com/kata/5a005f4fba2a14897f000086

def sum_it_up(numbers_with_bases):
    return sum(int(value, base) for value, base in numbers_with_bases)
