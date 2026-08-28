# Rank  : 6 kyu
# Title : Decipher this!
# Link  : https://www.codewars.com/kata/581e014b55f2c52bb00000f8


import re


def decipher_this(s):
    words = []
    for code, rest in re.findall(r"(\d+)(\w*)", s):
        first = chr(int(code))

        if len(rest) > 1:
            rest = rest[-1] + rest[1:-1] + rest[0]
        words.append(first + rest)
    return " ".join(words)


print(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"))
