# Rank  : 7 kyu
# Title : Simple string characters
# Link  : https://www.codewars.com/kata/5a29a0898f27f2d9c9000058


def solve(s):
    uppercase = lowercase = numbers = special_character = 0

    for c in s:
        if c.isupper():
            uppercase += 1
        elif c.islower():
            lowercase += 1
        elif c.isdigit():
            numbers += 1
        else:
            special_character += 1

    return [uppercase, lowercase, numbers, special_character]
