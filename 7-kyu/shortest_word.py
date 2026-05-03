# Rank  : 7 kyu
# Title : Shortest Word
# Link  : https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

def find_short(sentence):
    return min(len(word) for word in sentence.split())
