# Rank  : 6 kyu
# Title : Duplicate Encoder
# Link  : https://www.codewars.com/kata/54b42f9314d9229fd6000d9c


from collections import Counter


def duplicate_encode(word):
    table = Counter(word.casefold())
    return "".join(["(", ")"][table[key] > 1] for key in word.casefold())


print(duplicate_encode("din"), "(((")
print(duplicate_encode("recede"), "()()()")
print(duplicate_encode("Success"), ")())())")
print(duplicate_encode("(( @"), "))((")
