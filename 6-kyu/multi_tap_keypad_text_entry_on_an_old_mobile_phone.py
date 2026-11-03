# Rank  : 6 kyu
# Title : Multi-tap Keypad Text Entry on an Old Mobile Phone
# Link  : https://www.codewars.com/kata/54a2e93b22d236498400134b


def presses(phrase):
    total = 0

    for c in phrase.upper():
        if c in " ADGJMPTW1#*":
            total += 1
        elif c in "BEHKNQUX0":
            total += 2
        elif c in "CFILORVY":
            total += 3
        elif c in "SZ234568":
            total += 4
        elif c in "79":
            total += 5

    return total
