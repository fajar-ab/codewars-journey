# Rank  : 6 kyu
# Title : Where is my parent!?(cry)
# Link  : https://www.codewars.com/kata/58539230879867a8cd00011c


def find_children(dancing_brigade):
    return "".join(sorted(dancing_brigade, key=lambda c: (c.lower(), c.islower())))
