# Rank  : 7 kyu
# Title : Alternate capitalization
# Link  : https://www.codewars.com/kata/59cfc000aeb2844d16000075


def capitalize(s):
    return [
        "".join(c.upper() if i % 2 != 0 else c for i, c in enumerate(s)),
        "".join(c.upper() if i % 2 == 0 else c for i, c in enumerate(s)),
    ]
