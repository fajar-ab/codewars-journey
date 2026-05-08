# Rank  : 7 kyu
# Title : Beginner Series #3 Sum of Numbers
# Link  : https://www.codewars.com/kata/55f2b110f61eb01779000053

def get_sum(a,b):
    a, b = sorted([a, b])
    return sum(range(a, b+1))
