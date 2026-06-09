# Rank  : 8 kyu
# Title : Multiplication table for number
# Link  : https://www.codewars.com/kata/5a2fd38b55519ed98f0000ce


def multi_table(number):
    return "\n".join(f"{i} * {number} = {i * number}" for i in range(1, 11))


print(multi_table(1))
