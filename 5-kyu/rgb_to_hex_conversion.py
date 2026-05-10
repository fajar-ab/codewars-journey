# Rank  : 5 kyu
# Title : RGB To Hex Conversion
# Link  : https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    return "".join("{:02X}".format(max(0, min(255, value))) for value in [r, g, b])