# Rank  : 6 kyu
# Title : Unique In Order
# Link  : https://www.codewars.com/kata/54e6533c92449cc251001667

def unique_in_order(sequence):
    value = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i-1]:
            value.append(sequence[i])
    
    return value
