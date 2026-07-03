# Rank  : 8 kyu
# Title : Array Array Array
# Link  : https://www.codewars.com/kata/57eb936de1051801d500008a


def explode(arr):
    if all(type(el) is str for el in arr):
        return "Void!"

    score = sum(el for el in arr if type(el) is int)
    return [arr for _ in range(score)]
