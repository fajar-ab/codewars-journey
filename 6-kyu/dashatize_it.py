# Rank  : 6 kyu
# Title : Dashatize it
# Link  : https://www.codewars.com/kata/58223370aef9fc03fd000071


def dashatize(n):
    temp = "".join([f"-{num}-" if int(num) % 2 else num for num in str(n)])
    return temp.replace("--", "-").strip("-")


print(dashatize(6815))
