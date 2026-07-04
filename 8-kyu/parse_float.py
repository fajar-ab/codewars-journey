# Rank  : 8 kyu
# Title : Parse float
# Link  : https://www.codewars.com/kata/57a386117cb1f31890000039


def parse_float(string):
    try:
        return float(string)
    except (ValueError, TypeError):
        return None
