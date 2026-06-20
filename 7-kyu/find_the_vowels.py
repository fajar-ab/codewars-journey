# Rank  : 7 kyu
# Title : Find the vowels
# Link  : https://www.codewars.com/kata/5680781b6b7c2be860000036


def vowel_indices(word):
    return [i for i, c in enumerate(word.lower(), 1) if c in "aeiouy"]
