# Rank  : 8 kyu
# Title : Freudian translator
# Link  : https://www.codewars.com/kata/5713bc89c82eff33c60009f7


def to_freud(sentence):
    return " ".join(["sex"] * len(sentence.split()))


print(to_freud("You're becoming a true freudian expert"))
