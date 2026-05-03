# Rank  : 7 kyu
# Title : Vowel Count
# Link  : https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(sentence):
    return sum(1 for letter in sentence if letter in "aiueo")