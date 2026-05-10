# Rank  : 7 kyu
# Title : Alphabet war
# Link  : https://www.codewars.com/kata/59377c53e66267c8f6000027

def alphabet_war(fight):
    left_side = {"w": 4, "p": 3, "b": 2, "s": 1}
    right_side = {"m": 4, "q": 3, "d": 2, "z": 1}
    left_score, right_score = 0, 0

    for f in fight:
        if f in left_side: left_score += left_side[f]
        elif f in right_side: right_score += right_side[f]

    if left_score > right_score:
        result = "Left side wins!"
    elif left_score < right_score:
        result = "Right side wins!"
    else:
        result = "Let's fight again!"

    return result
