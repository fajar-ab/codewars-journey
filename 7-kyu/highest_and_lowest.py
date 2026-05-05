# Rank  : 7 kyu
# Title : Highest and Lowest
# Link  : https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):
    number_iter = list(map(int, numbers.split()))
    return f"{max(number_iter)} {min(number_iter)}"

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))