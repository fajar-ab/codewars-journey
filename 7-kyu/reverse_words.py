# Rank  : 7 kyu
# Title : Reverse words
# Link  : https://www.codewars.com/kata/5259b20d6021e9e14c0010d4

def reverse_words(text):
    return " ".join([txet[::-1] for txet in text.split()])
