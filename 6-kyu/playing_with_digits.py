# Rank  : 6 kyu
# Title : Playing with digits
# Link  : https://www.codewars.com/kata/5552101f47fc5178b1000050


def dig_pow(n, p):
    s = sum(int(number) ** i for i, number in enumerate(str(n), p))
    return s // n if s % n == 0 else -1


print(dig_pow(89, 1), 1)
