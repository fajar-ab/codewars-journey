# Rank  : 7 kyu
# Title : Palindromes Here and There
# Link  : https://www.codewars.com/kata/5838a66eaed8c259df000003


def convert_palindromes(numbers):
    return [int(n == n[::-1]) for n in map(str, numbers)]


print(convert_palindromes([101, 2, 85, 33, 14014]))
