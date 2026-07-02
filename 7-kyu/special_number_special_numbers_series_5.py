# Rank  : 7 kyu
# Title : Special Number (Special Numbers Series #5)
# Link  : https://www.codewars.com/kata/5a55f04be6be383a50000187


def special_number(number):
    return ("NOT!!", "Special!!")[all(n in "012345" for n in str(number))]
