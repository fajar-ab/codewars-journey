# Rank  : 7 kyu
# Title : Simple Fun #87: Shuffled Array
# Link  : https://www.codewars.com/kata/589573e3f0902e8919000109

def shuffled_array(numbers):
    numbers.sort()
    numbers.remove(sum(numbers) // 2)
    return numbers
