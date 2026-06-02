# Rank  : 6 kyu
# Title : Build Tower
# Link  : https://www.codewars.com/kata/576757b1df89ecf5bd00073b

def tower_builder(n_floors):
    pytramid = []

    for i in range(n_floors):
        star = "*" * (2 * i + 1)
        pytramid.append(star.center(2 * n_floors - 1))

    return pytramid
