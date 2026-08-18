# Rank  : 8 kyu
# Title : Logical calculator
# Link  : https://www.codewars.com/kata/57096af70dad013aa200007b


from functools import reduce


def logical_calc(array, op):
    ops = {
        "AND": lambda a, b: a and b,
        "OR": lambda a, b: a or b,
        "XOR": lambda a, b: a ^ b,
    }

    return reduce(ops.get(op), array)
