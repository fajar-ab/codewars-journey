# Rank  : 7 kyu
# Title : Summing a number's digits
# Link  : https://www.codewars.com/kata/52f3149496de55aded000410


def sum_digits(number):
    return sum(map(int, str(abs(number))))


print(sum_digits(10))
print(sum_digits(99))
print(sum_digits(-32))
