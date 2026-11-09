# Rank  : 7 kyu
# Title : Count all the sheep on farm in the heights of New Zealand
# Link  : https://www.codewars.com/kata/58e0f0bf92d04ccf0a000010


def lost_sheep(friday, saturday, total):
    return total - (sum(friday) + sum(saturday))
