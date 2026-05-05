# Rank  : 7 kyu
# Title : Highest and Lowest
# Link  : https://www.codewars.com/kata/reviews/5557d51de2da64b93200001b/groups/69fa04617e0d6b29b5ed75e7

def high_and_low(numbers):
    number_iter = list(map(int, numbers.split()))
    return f"{max(number_iter)} {min(number_iter)}"

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))