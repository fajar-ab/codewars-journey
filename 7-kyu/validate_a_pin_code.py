# Rank  : 7 kyu
# Title : Validate a PIN code
# Link  : https://www.codewars.com/kata/55f8a9c06c018a0d6e000132


import re

def validate_pin(pin):
    return bool(re.fullmatch(r"(\d{4}|\d{6})", pin))


