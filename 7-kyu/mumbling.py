# Rank  : 7 kyu
# Title : Mumbling
# Link  : https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

def accum(st):
    return "-".join([f"{st[i] * (i+1)}".capitalize() for i in range(len(st))])