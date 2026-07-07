# Rank  : 8 kyu
# Title : Grader
# Link  : https://www.codewars.com/kata/53d16bd82578b1fb5b00128c


def grader(score):
    return (
        "F"
        if score > 1 or score < 0.6
        else "A"
        if score >= 0.9
        else "B"
        if score >= 0.8
        else "C"
        if score >= 0.7
        else "D"
    )


print(grader(1), "A")
print(grader(1.01), "F")
print(grader(0.20), "F")
print(grader(0.70), "C")
print(grader(0.80), "B")
print(grader(0.90), "A")
print(grader(0.60), "D")
print(grader(0.50), "F")
print(grader(0.00), "F")
