# Rank  : 7 kyu
# Title : Numbers to Letters
# Link  : https://www.codewars.com/kata/57ebaa8f7b45ef590c00000c


def switcher(arr):
    table = "_zyxwvutsrqponmlkjihgfedcba!? "
    return "".join(table[int(n)] for n in arr)
