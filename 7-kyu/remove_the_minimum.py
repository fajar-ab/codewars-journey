# Rank  : 7 kyu
# Title : Remove the minimum
# Link  : https://www.codewars.com/kata/563cf89eb4747c5fb100001b

def remove_smallest(numbers):
    if copy := numbers[:]: 
        copy.remove(min(numbers))
        
    return copy

remove_smallest([])
remove_smallest([1, 2, 3, 4, 5])