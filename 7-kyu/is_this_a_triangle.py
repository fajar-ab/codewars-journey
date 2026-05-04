# Rank  : 7 kyu
# Title : Is this a triangle?
# Link  : https://www.codewars.com/kata/reviews/56d365af6e2572a5c000005f/groups/572b0fa04903c1a135000464

def is_triangle(a, b, c):
    """
    Syarat Ketaksamaan Segitiga
    - a + b > c
    - a + c > b
    - b + c > a
    """
    return all([a + b > c, a + c > b, b + c > a])
