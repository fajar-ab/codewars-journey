# Rank  : 8 kyu
# Title : Grasshopper Grade book
# Link  : https://www.codewars.com/kata/55cbd4ba903825f7970000f5

from statistics import mean

def get_grade(s1, s2, s3):
    score = mean([s1, s2, s3])

    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'

print(get_grade(95, 90, 93))    