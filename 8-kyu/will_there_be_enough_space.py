# Rank  : 8 kyu
# Title : Will there be enough space?
# Link  : https://www.codewars.com/kata/5875b200d520904a04000003

def enough(cap, on, wait):
    return -min(0, cap - (on + wait))

