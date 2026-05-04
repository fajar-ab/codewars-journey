# Rank  : 8 kyu
# Title : Convert boolean values to strings 'Yes' or 'No'
# Link  : https://www.codewars.com/kata/reviews/545878a4888e9859aa000210/groups/5825f8b422be6eec6400002b

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

print(bool_to_word(True))
print(bool_to_word(False))