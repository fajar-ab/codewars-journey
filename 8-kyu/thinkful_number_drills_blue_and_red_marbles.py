# Rank  : 8 kyu
# Title : Thinkful - Number Drills: Blue and red marbles
# Link  : https://www.codewars.com/kata/5862f663b4e9d6f12b00003b


def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    blue_left = blue_start - blue_pulled
    total_left = blue_start + red_start - blue_pulled - red_pulled

    return blue_left / total_left


print(guess_blue(5, 5, 2, 3), 0.6)
print(guess_blue(5, 7, 4, 3), 0.2)
print(guess_blue(12, 18, 4, 6), 0.4)
