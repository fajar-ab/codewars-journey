# Rank  : 7 kyu
# Title : Flatten
# Link  : https://www.codewars.com/kata/5250a89b1625e5decd000413


def flatten(lst):
    return [
        item
        for sublist in lst
        for item in (sublist if isinstance(sublist, list) else [sublist])
    ]
