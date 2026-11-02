# Rank  : 7 kyu
# Title : The Office III - Broken Photocopier
# Link  : https://www.codewars.com/kata/57ed56657b45ef922300002b


def broken(inp):
    return inp.translate(str.maketrans("10", "01"))


print(broken("101"))
