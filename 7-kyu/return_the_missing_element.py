# Rank  : 7 kyu
# Title : Return the Missing Element
# Link  : https://www.codewars.com/kata/5299413901337c637e000004


def get_missing_element(seq):
    lost, *_ = [n for n in range(10) if n not in seq]
    return lost
