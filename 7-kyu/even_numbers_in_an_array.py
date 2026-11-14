# Rank  : 7 kyu
# Title : Even numbers in an array
# Link  : https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c


def even_numbers(arr, n):
    return [n for n in arr if n % 2 == 0][-n:]


print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
