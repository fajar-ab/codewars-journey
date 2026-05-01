# Rank  : 6 kyu
# Title : Multiples of 3 or 5
# URL   : https://www.codewars.com/kata/reviews/54a5ebd237f4350faf00006c/groups/5e9c83a336c5250001bd3bc9

def solution(number):
    result = 0
    
    for num in range(number):
        if num % 3 == 0:
            result += num
        elif num % 5 == 0:
            result += num
    
    return result