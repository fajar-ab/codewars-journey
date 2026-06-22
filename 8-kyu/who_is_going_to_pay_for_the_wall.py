# Rank  : 8 kyu
# Title : Who is going to pay for the wall?
# Link  : https://www.codewars.com/kata/58bf9bd943fadb2a980000a7


def who_is_paying(name):
    return [name] if len(name) <= 2 else [name, name[:2]]
