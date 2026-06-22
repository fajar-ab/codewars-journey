# Rank  : 8 kyu
# Title : simple calculator
# Link  : https://www.codewars.com/kata/5810085c533d69f4980001cf


def calculator(x, y, op):
    if type(x) is int and type(y) is int and op in {"+", "-", "*", "/"}:
        return eval(f"{x} {op} {y}")

    return "unknown value"
