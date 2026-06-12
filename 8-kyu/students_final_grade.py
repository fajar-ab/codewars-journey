# Rank  : 8 kyu
# Title : Student's Final Grade
# Link  : https://www.codewars.com/kata/5ad0d8356165e63c140014d4


def final_grade(exam, projects):
    return (
        100
        if exam > 90 or projects > 10
        else 90
        if exam > 75 and projects >= 5
        else 75
        if exam > 50 and projects >= 2
        else 0
    )
