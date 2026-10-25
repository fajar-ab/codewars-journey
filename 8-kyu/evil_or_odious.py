# Rank  : 8 kyu
# Title : Evil or Odious
# Link  : https://www.codewars.com/kata/56fcfad9c7e1fa2472000034


def evil(n):
    return "It's Evil!" if n.bit_count() % 2 == 0 else "It's Odious!"
