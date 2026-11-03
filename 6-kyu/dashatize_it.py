# Rank  : 6 kyu
# Title : Dashatize it
# Link  : https://www.codewars.com/kata/58223370aef9fc03fd000071


import re


def dashatize(n):
    return "-".join(re.findall(r"[02468]+|[13579]", str(abs(n))))


print(dashatize(6815))
