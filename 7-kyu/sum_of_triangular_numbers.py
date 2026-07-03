# Rank  : 7 kyu
# Title : Sum of Triangular Numbers
# Link  : https://www.codewars.com/kata/580878d5d27b84b64c000b51


def sum_triangular_numbers(n):
    lst = []
    a = 0
    for i in range(1, n + 1):
        a = a + i
        lst.append(a)

    return sum(lst)
