# Rank  : 8 kyu
# Title : You only need one Beginner
# Link  : https://www.codewars.com/kata/reviews/57e922d73fad30057000004b/groups/69f97d947752f8e95dadf155

def check(seq, elem):
    index = 0
    while index < len(seq):
        if elem == seq[index]:
            return True
        index += 1
    return False

print(check([78, 117, 110, 99, 104, 117, 107, 115], 110))