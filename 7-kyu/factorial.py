# Rank  : 7 kyu
# Title : Factorial
# Link  : https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc


def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    elif n <= 1:
        return 1

    return n * factorial(n - 1)
