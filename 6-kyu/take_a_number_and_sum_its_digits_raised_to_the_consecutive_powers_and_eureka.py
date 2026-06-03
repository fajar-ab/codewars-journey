# Rank  : 6 kyu
# Title : Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!
# Link  : https://www.codewars.com/kata/5626b561280a42ecc50000d1

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    return [
        num for num in range(a, b+1)
        if num == sum(int(base) ** power for power, base in enumerate(str(num), 1))
    ]
