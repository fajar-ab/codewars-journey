# Rank  : 7 kyu
# Title : Balanced Number (Special Numbers Series #1 )
# Link  : https://www.codewars.com/kata/5a4e3782880385ba68000018


def balanced_num(number):
    digits = list(map(int, str(number)))
    n = len(digits)
    k = (n - 1) // 2

    return "Balanced" if sum(digits[:k]) == sum(digits[n - k :]) else "Not Balanced"


print(balanced_num(7), "Balanced")
print(balanced_num(959), "Balanced")
print(balanced_num(13), "Balanced")
print(balanced_num(432), "Not Balanced")
print(balanced_num(424), "Balanced")
