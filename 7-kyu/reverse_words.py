# Rank  : 7 kyu
# Title : Reverse words
# Link  : https://www.codewars.com/kata/reviews/547bbf3d2d47f7a96f0001ce/groups/69fa20fcdd8763af86f07108

def reverse_words(text):
    return " ".join([txet[::-1] for txet in text.split()])
