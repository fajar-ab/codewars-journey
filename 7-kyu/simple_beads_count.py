# Rank  : 7 kyu
# Title : Simple beads count
# Link  : https://www.codewars.com/kata/58712dfa5c538b6fc7000569


def count_red_beads(n):
    return len(["@", "@"] * (n - 1))
