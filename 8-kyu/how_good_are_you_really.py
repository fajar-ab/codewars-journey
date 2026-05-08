# Rank  : 8 kyu
# Title : How good are you really?
# Link  : https://www.codewars.com/kata/5601409514fc93442500010b

from statistics import mean

def better_than_average(class_points, your_points):
    return mean(class_points) <= your_points