# Rank  : 7 kyu
# Title : Switcheroo
# Link  : https://www.codewars.com/kata/57f759bb664021a30300007d


def switcheroo(s):
    return s.translate(str.maketrans("ab", "ba"))
