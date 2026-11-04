# Rank  : 6 kyu
# Title : Word a10n (abbreviation)
# Link  : https://www.codewars.com/kata/5375f921003bf62192000746


import re


def abbreviate_word(m):
    first, *middle, last = m.group()
    return f"{first}{len(middle)}{last}"


def abbreviate(s):
    return re.sub(r"[a-zA-Z]{4,}", abbreviate_word, s)


print(abbreviate("elephant-rides are really fun!"))
