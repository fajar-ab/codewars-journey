# Rank  : 7 kyu
# Title : The Office II - Boredom Score
# Link  : https://www.codewars.com/kata/57ed4cef7b45ef8774000014


def boredom(staff):
    skor = {
        "accounts": 1,
        "finance": 2,
        "canteen": 10,
        "regulation": 3,
        "trading": 6,
        "change": 6,
        "IS": 8,
        "retail": 5,
        "cleaning": 4,
        "pissing about": 25,
    }

    total = 0
    for value in staff.values():
        total += skor[value]

    return (
        "kill me now"
        if total <= 80
        else "i can handle this"
        if 80 < total < 100
        else "party time!!"
    )
