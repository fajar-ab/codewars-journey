# Rank  : 8 kyu
# Title : Power
# Link  : https://www.codewars.com/kata/562926c855ca9fdc4800005b


def number_to_pwr(number, p):
    if p < 1:
        return 1

    return number * number_to_pwr(number, p - 1)


print(number_to_pwr(4, 2))
