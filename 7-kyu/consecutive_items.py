# Rank  : 7 kyu
# Title : Consecutive items
# Link  : https://www.codewars.com/kata/5f6d533e1475f30001e47514


def consecutive(arr, a, b):
    posisi_a = arr.index(a)
    posisi_b = arr.index(b)

    return abs(posisi_a - posisi_b) == 1
