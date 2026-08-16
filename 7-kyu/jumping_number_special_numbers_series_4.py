# Rank  : 7 kyu
# Title : Jumping Number (Special Numbers Series #4)
# Link  : https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed


def jumping_number(number):
    number = list(map(int, str(number)))

    for i in range(len(number) - 1):
        if abs(number[i] - number[i + 1]) != 1:
            return "Not!!"

    return "Jumping!!"
