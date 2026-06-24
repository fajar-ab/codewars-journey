# Rank  : 8 kyu
# Title : Surface Area and Volume of a Box
# Link  : https://www.codewars.com/kata/565f5825379664a26b00007c


def get_size(width, height, depth):
    return [
        2 * (width * depth + width * height + depth * height),
        (width * height * depth),
    ]
