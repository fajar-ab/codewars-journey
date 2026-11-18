# Rank  : 7 kyu
# Title : Word values
# Link  : https://www.codewars.com/kata/598d91785d4ce3ec4f000018


def name_value(my_list):
    return [
        sum(ord(c) - 96 for c in value if c.isalpha()) * i
        for i, value in enumerate(my_list, 1)
    ]


print(name_value(["codewars", "abc", "xyz"]))
