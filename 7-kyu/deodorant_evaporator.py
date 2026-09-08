# Rank  : 7 kyu
# Title : Deodorant Evaporator
# Link  : https://www.codewars.com/kata/5506b230a11c0aeab3000c1f


def evaporator(content, evap_per_day, threshold):
    sisa = 100
    n = 0

    while sisa > threshold:
        sisa = sisa * ((100 - evap_per_day) / 100)
        n += 1

    return n
