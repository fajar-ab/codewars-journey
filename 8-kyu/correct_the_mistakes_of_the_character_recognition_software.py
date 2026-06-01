# Rank  : 8 kyu
# Title : Correct the mistakes of the character recognition software
# Link  : https://www.codewars.com/kata/577bd026df78c19bca0002c0

def correct(s):
    correct = str.maketrans({
        "5": "S",
        "0": "O",
        "1": "I"
    })

    return s.translate(correct)

