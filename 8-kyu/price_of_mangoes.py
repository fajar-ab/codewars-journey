# Rank  : 8 kyu
# Title : Price of Mangoes
# Link  : https://www.codewars.com/kata/57a77726bb9944d000000b06/train/python"


def mango(quantity, price):
    return len(["🥭" for n in range(1, quantity + 1) if n % 3]) * price
