# Rank  : 7 kyu
# Title : Shortest Word
# Link  : https://www.codewars.com/kata/reviews/57cf0c8d50c3e50133000055/groups/57cf465a902f6b65ed0000c9

def find_short(sentence):
    return min(len(word) for word in sentence.split())
