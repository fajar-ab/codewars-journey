# Rank  : 7 kyu
# Title : Divide and Conquer
# Link  : https://www.codewars.com/kata/57eaec5608fed543d6000021


def div_con(x):
    return sum(n for n in x if type(n) is int) - sum(
        int(s) for s in x if type(s) is str
    )


print(div_con([9, 3, "7", "3"]))
