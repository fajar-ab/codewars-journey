# Rank  : 6 kyu
# Title : Unique In Order
# Link  : https://www.codewars.com/kata/reviews/54e659a9e323fec7c30002a7/groups/69f8aff1bd7c7ebfc5a279b9

def unique_in_order(sequence):
    value = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i-1]:
            value.append(sequence[i])
    
    return value
