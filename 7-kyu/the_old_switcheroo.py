# Rank  : 7 kyu
# Title : The old switcheroo
# Link  : https://www.codewars.com/kata/55d410c492e6ed767000004f


def vowel_2_index(string):
    return "".join(
        str(index) if char in "aeiouAEIOU" else char
        for index, char in enumerate(string, 1)
    )
