# Rank  : 7 kyu
# Title : Mumbling
# Link  : https://www.codewars.com/kata/reviews/5667e9e7ffbf34676800005f/groups/69f5c307db05bea0b40adee1

def accum(st):
    return "-".join([f"{st[i] * (i+1)}".capitalize() for i in range(len(st))])