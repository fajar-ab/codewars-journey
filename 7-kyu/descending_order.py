# Rank  : 7 kyu
# Title : Descending Order
# Link  : https://www.codewars.com/kata/5467e4d82edf8bbf40000155

def descending_order(num):
    s = sorted(str(num), reverse=True)
    return int("".join(s))
