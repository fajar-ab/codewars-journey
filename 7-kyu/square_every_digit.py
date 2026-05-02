# Rank  : 7 kyu
# Title : Square Every Digit
# Link  : https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    digits = map(int, str(num))
    square = [digit ** 2 for digit in digits]
    combine = int("".join(map(str, square)))

    return combine
