# Rank  : 8 kyu
# Title : Did she say hallo?
# Link  : https://www.codewars.com/kata/56a4addbfd4a55694100001f


import re


def validate_hello(greetings):
    return bool(re.search(r"h[ae]llo|ciao|salut|hola|ahoj|czesc", greetings, re.I))
