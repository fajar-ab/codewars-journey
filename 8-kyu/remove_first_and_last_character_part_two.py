# Rank  : 8 kyu
# Title : Remove First and Last Character Part Two
# Link  : https://www.codewars.com/kata/570597e258b58f6edc00230d


def array(string):
    num = string.split(",")
    return None if len(num) < 3 else " ".join(c for c in num[1:-1])
