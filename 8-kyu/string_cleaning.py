# Rank  : 8 kyu
# Title : String cleaning
# Link  : https://www.codewars.com/kata/57e1e61ba396b3727c000251


def string_clean(s):
    return "".join(c for c in s if not c.isdigit())
