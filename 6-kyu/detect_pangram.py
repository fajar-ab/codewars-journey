# Rank  : 6 kyu
# Title : Detect Pangram
# Link  : https://www.codewars.com/kata/545cedaa9943f7fe7b000048


from string import ascii_lowercase as alphabet


def is_pangram(st):
    return all(c in st for c in alphabet)
