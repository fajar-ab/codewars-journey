# Rank  : 7 kyu
# Title : Make a function that does arithmetic!
# Link  : https://www.codewars.com/kata/583f158ea20cfcbeb400000a

from operator import add, sub, mul, truediv

def arithmetic(a, b, operator):
    ops = {
        "add": add, 
        "subtract": sub, 
        "multiply": mul, 
        "divide": truediv
    }

    return ops[operator](a, b)

