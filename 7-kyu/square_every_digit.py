# Rank  : 7 kyu
# Title : Square Every Digit
# Link  : https://www.codewars.com/kata/reviews/546e2568b03326a88e000022/groups/69f5d67ddb05bea0b40ae02d

def square_digits(num):
    digits = map(int, str(num))
    square = [digit ** 2 for digit in digits]
    combine = int("".join(map(str, square)))

    return combine
