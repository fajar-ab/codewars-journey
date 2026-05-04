# Rank  : 7 kyu
# Title : Simple Fun #87: Shuffled Array
# Link  : https://www.codewars.com/kata/reviews/5895d1a04839ffdfb3001973/groups/69f8121733302911ec6daf56

def shuffled_array(numbers):
    numbers.sort()
    numbers.remove(sum(numbers) // 2)
    return numbers
