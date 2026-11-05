# Rank  : 7 kyu
# Title : Find the nth Digit of a Number
# Link  : https://www.codewars.com/kata/577b9960df78c19bca00007e


def find_digit(num, nth):
    digit = str(abs(num))[::-1]
    
    if nth <= 0:
        return -1
    if len(digit) < nth:
        return 0

    return int(digit[nth-1])
