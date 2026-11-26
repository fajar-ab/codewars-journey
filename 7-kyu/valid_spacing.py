# Rank  : 7 kyu
# Title : Valid Spacing
# Link  : https://www.codewars.com/kata/5f77d62851f6bc0033616bd8


def valid_spacing(s):
    return s == " ".join(s.split())


print(valid_spacing("hello world"))
