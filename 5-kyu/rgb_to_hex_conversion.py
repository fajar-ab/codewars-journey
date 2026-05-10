# Rank  : 5 kyu
# Title : RGB To Hex Conversion
# Link  : https://www.codewars.com/kata/513e08acc600c94f01000001

def rgb(r, g, b):
    round = lambda x: max(min(x, 255), 0)
    return ("{:02X}" * 3).format(round(r), round(g), round(b))