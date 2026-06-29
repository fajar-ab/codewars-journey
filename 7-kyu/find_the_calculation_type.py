# Rank  : 7 kyu
# Title : Find the calculation type
# Link  : https://www.codewars.com/kata/5aca48db188ab3558e0030fa


def calc_type(a, b, res) -> str:
    ops = {
        "addition": lambda a, b: a + b,
        "subtraction": lambda a, b: a - b,
        "multiplication": lambda a, b: a * b,
        "division": lambda a, b: a / b,
    }

    for operator, func in ops.items():
        if func(a, b) == res:
            return operator
