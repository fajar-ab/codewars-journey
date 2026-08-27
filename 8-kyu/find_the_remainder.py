# Rank  : 8 kyu
# Title : Find the Remainder
# Link  : https://www.codewars.com/kata/524f5125ad9c12894e00003f


def remainder(a, b):
    if b > a:
        return remainder(b, a)

    try:
        return a % b
    except ZeroDivisionError:
        return None
