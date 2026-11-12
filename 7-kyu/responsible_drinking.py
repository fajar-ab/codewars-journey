# Rank  : 7 kyu
# Title : Responsible Drinking
# Link  : https://www.codewars.com/kata/5aee86c5783bb432cd000018


def hydrate(drink_string):
    total = sum(int(n) for n in drink_string.split() if n.isdigit())
    return f"{total} {'glass' if total == 1 else 'glasses'} of water"
