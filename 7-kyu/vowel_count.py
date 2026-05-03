# Rank  : 7 kyu
# Title : Vowel Count
# Link  : https://www.codewars.com/kata/reviews/54ff37ee355cfd937000105c/groups/65c0eebe6b29d80001cf5ba1

def get_count(sentence):
    return sum(1 for letter in sentence if letter in "aiueo")