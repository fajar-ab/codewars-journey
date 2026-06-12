# Rank  : 8 kyu
# Title : Remove duplicates from list
# Link  : https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118


def distinct(seq):
    return list(dict.fromkeys(seq))
