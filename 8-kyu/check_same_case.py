# Rank  : 8 kyu
# Title : Check same case
# Link  : https://www.codewars.com/kata/5dd462a573ee6d0014ce715b/train/python


def same_case(a, b):
    return (
        -1
        if not a.isalpha() or not b.isalpha()
        else 1
        if a.islower() and b.islower() or a.isupper() and b.isupper()
        else 0
    )
