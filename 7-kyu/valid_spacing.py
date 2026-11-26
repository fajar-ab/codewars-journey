# Rank  : 7 kyu
# Title : Valid Spacing
# Link  : https://www.codewars.com/kata/5f77d62851f6bc0033616bd8

import re


def valid_spacing(s):
    return bool(re.search(r"^(?! )(?!.* $)(?!.* {2}).*$", s))


print(valid_spacing("hello world"))
