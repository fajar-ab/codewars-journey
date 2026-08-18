# Rank  : 8 kyu
# Title : Logical calculator
# Link  : https://www.codewars.com/kata/57096af70dad013aa200007b


from functools import reduce


def logical_calc(array, op):
    oper = {"AND": "and", "OR": "or", "XOR": "^"}
    return reduce(lambda a, b: eval(f"{a} {oper.get(op)} {b}"), array)
