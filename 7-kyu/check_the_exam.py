# Rank  : 7 kyu
# Title : Check the exam
# Link  : https://www.codewars.com/kata/5a3dd29055519e23ec000074


def check_exam(arr1, arr2):
    point = 0
    for a, b in zip(arr1, arr2):
        point += 4 if a == b else (-1 if b else 0)

    return max(0, point)
