# Rank  : 8 kyu
# Title : The Feast of Many Beasts
# Link  : https://www.codewars.com/kata/5aa736a455f906981800360d

def feast(beast, dish):
    return all((beast[0] == dish[0], beast[-1] == dish[-1]))

print(feast("great blue heron", "garlic naan"))