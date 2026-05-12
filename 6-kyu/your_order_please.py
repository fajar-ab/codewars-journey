# Rank  : 6 kyu
# Title : Your order, please
# Link  : https://www.codewars.com/kata/55c45be3b2079eccff00010f

from re import findall

def order(sentence):
    words = sentence.split()
    words_sort = sorted(words, key=lambda w: findall(r"\d+", w)[0])
    return " ".join(words_sort)

print(order("4of Fo1r pe6ople g3ood th5e the2"))