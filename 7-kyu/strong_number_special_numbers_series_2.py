# Rank  : 7 kyu
# Title : Strong Number (Special Numbers Series #2)
# Link  : https://www.codewars.com/kata/5a4d303f880385399b000001


from math import factorial


def strong_num(number):
    sum_factorial = sum(factorial(int(n)) for n in str(number))
    return ("Not Strong !!", "STRONG!!!!")[number == sum_factorial]
