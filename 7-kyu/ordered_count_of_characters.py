# Rank  : 7 kyu
# Title : Ordered Count of Characters
# Link  : https://www.codewars.com/kata/57a6633153ba33189e000074

def ordered_count(inp):
    count_alfabet = {}

    for alfabet in inp:
        if alfabet not in count_alfabet:
            count_alfabet[alfabet] = 1
            continue
        
        count_alfabet[alfabet] += 1

    return list(count_alfabet.items())

