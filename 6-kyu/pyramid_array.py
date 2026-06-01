# Rank  : 6 kyu
# Title : Pyramid Array
# Link  : https://www.codewars.com/kata/515f51d438015969f7000013

def pyramid(n):
    subarrays = []
    
    for i in range(n):
        subarrays.append([1 for _ in range(i+1)])

    return subarrays