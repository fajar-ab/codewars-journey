# Rank  : 7 kyu
# Title : Find the capitals
# Link  : https://www.codewars.com/kata/539ee3b6757843632d00026b

def capitals(word):
    return [i for i, w in enumerate(word) if w.isupper()]
