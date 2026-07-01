# Rank  : 8 kyu
# Title : Simple validation of a username with regex
# Link  : https://www.codewars.com/kata/56a3f08aa9a6cc9b75000023


import re


def validate_usr(username):
    return bool(re.match(r"^[a-z0-9_]{4,16}$", username))
