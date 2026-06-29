# Rank  : 7 kyu
# Title : Printer Errors
# Link  : https://www.codewars.com/kata/56541980fa08ab47a0000040


from re import findall


def printer_error(s):
    return "{}/{}".format(len(findall(r"[^a-m]", s)), len(s))
