# Rank  : 7 kyu
# Title : Discover The Original Price
# Link  : https://www.codewars.com/kata/552564a82142d701f5001228


def discover_original_price(discounted_price, sale_percentage):
    return discounted_price / (1 - (sale_percentage / 100))
