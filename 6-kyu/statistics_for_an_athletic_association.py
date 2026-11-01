# Rank  : 6 kyu
# Title : Statistics for an Athletic Association
# Link  : https://www.codewars.com/kata/55b3425df71c1201a800009c


import statistics
import time
from datetime import datetime


def format(detik):
    return time.strftime("%H|%M|%S", time.gmtime(detik))


def stat(strg):
    if not strg:
        return ""

    tabel = []

    for value in strg.split(", "):
        waktu = datetime.strptime(value, "%H|%M|%S")
        tabel.append(waktu.hour * 3600 + waktu.minute * 60 + waktu.second)

    selisih = max(tabel) - min(tabel)
    rata_rata = statistics.mean(tabel)
    median = statistics.median(tabel)

    return f"Range: {format(selisih)} Average: {format(rata_rata)} Median: {format(median)}"


print(stat("01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"))
