# Rank  : 8 kyu
# Title : Calculate Price Excluding VAT
# Link  : https://www.codewars.com/kata/5890d8bc9f0f422cf200006b


def excluding_vat_price(price):
    if price is not None:
        return round(price / 1.15, 2)

    return -1
