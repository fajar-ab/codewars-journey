# Rank  : 7 kyu
# Title : Digital cypher
# Link  : https://www.codewars.com/kata/592e830e043b99888600002d


def encode(message, key):
    letters_encrypted = lambda c: ord(c) - 96
    keys = list(map(int, str(key)))

    return [letters_encrypted(l) + keys[i % len(keys)] for i, l in enumerate(message)]


print(encode("scout", 1939))
