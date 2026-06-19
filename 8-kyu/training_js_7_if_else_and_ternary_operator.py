# Rank  : 8 kyu
# Title : Training JS #7: if..else and ternary operator
# Link  : https://www.codewars.com/kata/57202aefe8d6c514300001fd


def sale_hotdogs(n):
    price_per_unit = 100 if n < 5 else 95 if 5 <= n < 10 else 90
    return n * price_per_unit


assert sale_hotdogs(0) == 0
assert sale_hotdogs(1) == 100
assert sale_hotdogs(2) == 200
assert sale_hotdogs(3) == 300
assert sale_hotdogs(4) == 400
assert sale_hotdogs(5) == 475
assert sale_hotdogs(9) == 855
assert sale_hotdogs(10) == 900
assert sale_hotdogs(11) == 990
assert sale_hotdogs(100) == 9000
