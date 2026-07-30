# Rank  : 7 kyu
# Title : Return the first M multiples of N
# Link  : https://www.codewars.com/kata/593c9175933500f33400003e


def multiples(m: int, n: int | float) -> list[int] | list[float]:
    return [n * i for i in range(1, m + 1)]
