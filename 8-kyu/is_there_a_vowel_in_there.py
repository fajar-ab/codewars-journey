# Rank  : 8 kyu
# Title : Is there a vowel in there?
# Link  : https://www.codewars.com/kata/57cff961eca260b71900008f


def is_vow(inp):
    return [c if (c := chr(num)) in "aeiou" else num for num in inp]
