# Rank  : 7 kyu
# Title : Predict your age!
# Link  : https://www.codewars.com/kata/5aff237c578a14752d0035ae


from math import sqrt


def predict_age(*age):
    return sqrt(sum(x * x for x in age)) // 2
