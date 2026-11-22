# Rank  : 6 kyu
# Title : Consecutive strings
# Link  : https://www.codewars.com/kata/56a5d994ac971f1ac500003e


def longest_consec(strarr, k):
    if k <= 0 or k > len(strarr):
        return ""

    return max(
        ("".join(strarr[i : i + k]) for i in range(len(strarr) - k + 1)), key=len
    )
