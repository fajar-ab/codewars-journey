# Rank  : 7 kyu
# Title : Friend or Foe?
# Link  : https://www.codewars.com/kata/55b42574ff091733d900002f

def friend(x):
    return list(filter(lambda name: len(name) == 4, x))
