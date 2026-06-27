# Rank  : 7 kyu
# Title : Disemvowel Trolls
# Link  : https://www.codewars.com/kata/52fba66badcd10859f00097e


def disemvowel(string_):
    return string_.translate(str.maketrans(dict.fromkeys("aeiuoAEIOU", "")))
