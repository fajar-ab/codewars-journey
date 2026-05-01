# Rank  : 6 kyu
# Title : Convert string to camel case
# URL   : https://www.codewars.com/kata/reviews/550b3a030681518093000205/groups/69f378a0e5037813cd98b4cf

def to_camel_case(text):
    if not text: return ""
        
    word_list = text.replace("-", " ").replace("_", " ").split()
    for i in range(len(word_list)):
        if i >= 1: word_list[i] = word_list[i].capitalize()

    return "".join(word_list)