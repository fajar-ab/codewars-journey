# Rank  : 8 kyu
# Title : Holiday VIII - Duty Free
# Link  : https://www.codewars.com/kata/57e92e91b63b6cbac20001e5


def duty_free(price, discount, holiday_cost):
    return holiday_cost // (price * (discount / 100))


assert duty_free(12, 50, 1000) == 166
assert duty_free(17, 10, 500) == 294
