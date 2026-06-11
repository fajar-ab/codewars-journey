# Rank  : 6 kyu
# Title : Tribonacci Sequence
# Link  : https://www.codewars.com/kata/556deca17c58da83c00002db


def tribonacci(signature, n):
    a, b, c = signature
    result = []

    for _ in range(n):
        result.append(a)
        a, b, c = b, c, a + b + c

    return result


print(tribonacci([1, 1, 1], 10))
