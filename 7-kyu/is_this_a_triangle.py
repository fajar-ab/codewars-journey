# Rank  : 7 kyu
# Title : Is this a triangle?
# Link  : https://www.codewars.com/kata/56606694ec01347ce800001b

def is_triangle(a, b, c):
    """
    Syarat Ketaksamaan Segitiga
    - a + b > c
    - a + c > b
    - b + c > a
    """
    return all([a + b > c, a + c > b, b + c > a])
