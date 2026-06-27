# Rank  : 8 kyu
# Title : Tip Calculator
# Link  : https://www.codewars.com/kata/56598d8076ee7a0759000087

from math import ceil


def calculate_tip(amount, rating):
    tip = {
        "terrible": ceil(amount * 0.0),
        "poor": ceil(amount * 0.05),
        "good": ceil(amount * 0.1),
        "great": ceil(amount * 0.15),
        "excellent": ceil(amount * 0.2),
    }

    return tip.get(rating.lower(), "Rating not recognised")
