# Rank  : 7 kyu
# Title : Maximum Length Difference
# Link  : https://www.codewars.com/kata/5663f5305102699bad000056


def mxdiflg(a1, a2):
    if a1 and a2:
        k1 = abs(len(min(a1, key=len)) - len(max(a2, key=len)))
        k2 = abs(len(min(a2, key=len)) - len(max(a1, key=len)))

        return max(k1, k2)

    return -1


a1 = [
    "hoqq",
    "bbllkw",
    "oox",
    "ejjuyyy",
    "plmiis",
    "xxxzgpsssa",
    "xxwwkktt",
    "znnnnfqknaz",
    "qqquuhii",
    "dvvvwz",
]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
print(mxdiflg(a1, a2))  # 13
