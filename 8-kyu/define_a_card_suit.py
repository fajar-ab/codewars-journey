# Rank  : 8 kyu
# Title : Define a card suit
# Link  : https://www.codewars.com/kata/5a360620f28b82a711000047


def define_suit(card):
    return {
        "C": "clubs",
        "D": "diamonds",
        "H": "hearts",
        "S": "spades",
    }.get(card[-1])
