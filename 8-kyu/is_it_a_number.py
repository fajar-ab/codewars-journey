# Rank  : 8 kyu
# Title : Is it a number?
# Link  : https://www.codewars.com/kata/57126304cdbf63c6770012bd


def is_digit(s):
    try:
        float(s.strip())
        return True
    except ValueError:
        return False




