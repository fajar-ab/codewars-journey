# Rank  : 7 kyu
# Title : Do They Agree?
# Link  : https://www.codewars.com/kata/6a2deeb1a8b6a4b0a80430af


def do_they_agree(alice, bob):
    return [n for n in alice if n in bob] == [n for n in bob if n in alice]
