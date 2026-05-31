# Rank  : 6 kyu
# Title : Counting Duplicates
# Link  : https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

from collections import Counter

def duplicate_count(text):
    return sum([1 for b in Counter(text.upper()).values() if b > 1])
     

print(duplicate_count(""))
print(duplicate_count("abcde"))
print(duplicate_count("abcdeaa"))
print(duplicate_count("abcdeaB"))