# Rank  : 7 kyu
# Title : shorter concat [reverse longer]
# Link  : https://www.codewars.com/kata/54557d61126a00423b000a45


def shorter_reverse_longer(a, b):
    if len(a) >= len(b):
        shorter, longer = b, a
    else:
        shorter, longer = a, b

    return shorter + longer[::-1] + shorter
