# Rank  : 7 kyu
# Title : Looking for a benefactor
# Link  : https://www.codewars.com/kata/569b5cec755dd3534d00000f

import math


def new_avg(arr, newavg):
    needed = math.ceil(newavg * (len(arr) + 1) - sum(arr))

    if needed <= 0:
        raise ValueError("Target rata-rata terlalu rendah")

    return needed


print(new_avg([14, 30, 5, 7, 9, 11, 15], 92))
