# Rank  : 7 kyu
# Title : Basic Calculator
# Link  : https://www.codewars.com/kata/5296455e4fe0cdf2e000059f


def calculate(num1, operation, num2):
    try:
        result = eval(f"{num1} {operation} {num2}")
        return result

    except (ZeroDivisionError, SyntaxError):
        return None
