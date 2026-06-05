# Rank  : 6 kyu
# Title : Multiplication table
# Link  : https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08


def multiplication_table(size):
    table = []
    for i in range(1, size + 1):
        table.append([num * i for num in range(1, size + 1)])

    return table
