# Rank  : 8 kyu
# Title : Grasshopper - Terminal game combat function
# Link  : https://www.codewars.com/kata/586c1cf4b98de0399300001d


def combat(health, damage):
    return max(0, health - damage)
