# Rank  : 6 kyu
# Title : Count the smiley faces!
# Link  : https://www.codewars.com/kata/583203e6eb35d7980400002a


import re


def count_smileys(arr):
    return sum(len(re.findall(r"[:;][~-]?[)D]", face)) for face in arr)
