# Rank  : 7 kyu
# Title : Char Code Calculation
# Link  : https://www.codewars.com/kata/57f75cc397d62fc93d000059


def calc(x):
    total = "".join(str(ord(s)) for s in x)
    return sum(map(int, total)) - sum(map(int, total.replace("7", "1")))


print(calc("abcdef"))
