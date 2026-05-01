# Rank  : 6 kyu
# Title : Multiples of 3 or 5
# Link  : https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    result = 0
    
    for num in range(number):
        if num % 3 == 0:
            result += num
        elif num % 5 == 0:
            result += num
    
    return result