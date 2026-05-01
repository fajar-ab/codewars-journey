# Rank  : 6 kyu
# Title : Convert string to camel case
# Link  : https://www.codewars.com/kata/517abf86da9663f1d2000003

def to_camel_case(text):
    if not text: return ""
        
    word_list = text.replace("-", " ").replace("_", " ").split()
    for i in range(len(word_list)):
        if i >= 1: word_list[i] = word_list[i].capitalize()

    return "".join(word_list)