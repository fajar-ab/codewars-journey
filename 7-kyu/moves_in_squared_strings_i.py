# Rank  : 7 kyu
# Title : Moves in squared strings (I)
# Link  : https://www.codewars.com/kata/56dbe0e313c2f63be4000b25


def vert_mirror(strng):
    return "\n".join(teks[::-1] for teks in strng.split("\n"))


def hor_mirror(strng):
    return "\n".join(reversed([teks for teks in strng.split("\n")]))


def oper(fct, s):
    return fct(s)
