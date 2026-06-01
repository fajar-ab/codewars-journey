# Rank  : 7 kyu
# Title : Anagram Detection
# Link  : https://www.codewars.com/kata/529eef7a9194e0cbc1000255

def is_anagram(test, original):
    return sorted(test.casefold()) == sorted(original.casefold())
