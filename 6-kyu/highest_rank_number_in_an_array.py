# Rank  : 6 kyu
# Title : Highest Rank Number in an Array
# Link  : https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004


def highest_rank(arr):
    return max(filter(lambda n: arr.count(n) == max(map(arr.count, arr)), arr))


print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]))
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]))
print(highest_rank([1, 2, 3]))
