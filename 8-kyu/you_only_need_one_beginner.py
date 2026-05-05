# Rank  : 8 kyu
# Title : You only need one Beginner
# Link  : https://www.codewars.com/kata/57cc975ed542d3148f00015b

def check(seq, elem):
    index = 0
    while index < len(seq):
        if elem == seq[index]:
            return True
        index += 1
    return False

print(check([78, 117, 110, 99, 104, 117, 107, 115], 110))