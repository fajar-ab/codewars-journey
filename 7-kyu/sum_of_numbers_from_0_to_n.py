# Rank  : 7 kyu
# Title : Sum of numbers from 0 to N
# Link  : https://www.codewars.com/kata/56e9e4f516bcaa8d4f001763


def show_sequence(n):
    return (
        "0=0"
        if n == 0
        else f"{n}<0"
        if n < 0
        else f"{'+'.join(map(str, range(n + 1)))} = {sum(range(n + 1))}"
    )
