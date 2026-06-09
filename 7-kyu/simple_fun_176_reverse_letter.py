# Rank  : 7 kyu
# Title : Simple Fun #176: Reverse Letter
# Link  : https://www.codewars.com/kata/58b8c94b7df3f116eb00005b


def reverse_letter(st):
    return "".join(c for c in st[::-1] if c.isalpha())
