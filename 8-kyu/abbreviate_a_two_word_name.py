# Rank  : 8 kyu
# Title : Abbreviate a Two Word Name
# Link  : https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3

def abbrev_name(name):
    return ".".join(n[0] for n in name.split()).upper()

print(abbrev_name("Sam Harris"))