# Rank  : 7 kyu
# Title : The Office III - Broken Photocopier
# Link  : https://www.codewars.com/kata/57ed56657b45ef922300002b


def broken(inp):
    return "".join(str(int(not bool(int(n)))) for n in inp)


print(broken("101"))
