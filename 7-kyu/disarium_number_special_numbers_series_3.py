# Rank  : 7 kyu
# Title : Disarium Number (Special Numbers Series #3)
# Link  : https://www.codewars.com/kata/5a53a17bfd56cb9c14000003


def disarium_number(number):
    is_disarium = number == sum(n**i for i, n in enumerate(map(int, str(number)), 1))
    return "Disarium !!" if is_disarium else "Not !!"


print(disarium_number(89))
