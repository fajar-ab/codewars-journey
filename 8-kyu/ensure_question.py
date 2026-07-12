# Rank  : 8 kyu
# Title : Ensure question
# Link  : https://www.codewars.com/kata/5866fc43395d9138a7000006


def ensure_question(s):
    return s if s.endswith("?") else s + "?"
