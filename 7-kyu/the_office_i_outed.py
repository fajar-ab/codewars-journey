# Rank  : 7 kyu
# Title : The Office I - Outed
# Link  : https://www.codewars.com/kata/57ecf6efc7fe13eb070000e1


def outed(meet, boss):
    happiness = sum(val * 2 if key == boss else val for key, val in meet.items()) / len(
        meet
    )
    return "Get Out Now!" if happiness <= 5 else "Nice Work Champ!"
